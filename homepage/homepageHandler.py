from zipcodes.models import Zipcode
from message.models import Message
from age.models import Age
from homepage.models import State, County, Gender, DisplayAge, USTimeGraphJson, TopMetrics
from django.db.models import Sum, Count
import datetime

TOTAL_BUCKETS = 10

def assignBuckets(states):
	num_states = len(states)
	per_bucket = 1.0
	if (num_states > TOTAL_BUCKETS):
		per_bucket = float(num_states) / float(TOTAL_BUCKETS)
	curr_bucket = TOTAL_BUCKETS-1
	counter = 0
	for s in states:
		s['bucket'] = curr_bucket
		counter += 1
		if counter >= per_bucket:
			counter = 0
			curr_bucket -= 1

def orderZipcodesIntoSortedStates():
	states = Zipcode.objects.values('state') \
		.annotate(num_male_cases=Sum('malePatientCases'), num_female_cases=Sum('femalePatientCases'))
	states = sorted(states, key=lambda state: - state['num_male_cases'] - state['num_female_cases'])
	assignBuckets(states)
	states = [State().populate(s['state'], s['num_male_cases'], s['num_female_cases'], s['bucket']) for s in states]
	return states

def orderCountiesFromState(state):
	counties = Zipcode.objects.filter(state__exact = state) \
		.values('county') \
		.annotate(num_male_cases=Sum('malePatientCases'), num_female_cases=Sum('femalePatientCases'))
	counties = sorted(counties, key=lambda county: county['num_male_cases'] + county['num_female_cases'])
	assignBuckets(counties)
	counties = [County().populate(c['county'], c['num_male_cases'], c['num_female_cases'], c['bucket']) for c in counties]
	return counties

def orderMessagesIntoSortedStates():
	messages = Message.objects.values('state')
	print(messages)

def getTopZipcodes():
	return Zipcode.objects.extra(
		select={'num_cases':'malePatientCases + femalePatientCases'},
		order_by=['-num_cases'])[:5]

def getTopDrug():
	product = Message.objects.values('productCode').annotate(num=Count('productCode')).order_by('-num')[0:5]
	return product[0]['productCode']

def orderGenderFromState(state):
	zipcodes = Zipcode.objects.filter(state__exact = state)
	gender = Gender().populate(state)
	for zipcode in zipcodes:
		gender.male += zipcode.malePatientCases
		gender.female += zipcode.femalePatientCases
	return gender

def orderAgeFromState(state):
	ages = Age.objects.filter(state__exact=state).values('age').annotate(num_cases=Sum('num_cases'))
	ages = [DisplayAge().populate(a['age'], a['num_cases']) for a in ages]
	return ages

def orderMessagesIntoState(state):
	messages = Message.objects.filter(state__exact=state).values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	messages = [USTimeGraphJson().populate(m['writtenDate'], m['num']) for m in messages]
	return messages

def getTopMetrics(state):
	data = TopMetrics()
	# calculate worstZipcode
	worstZipcodes = Zipcode.objects.filter(state__exact=state).extra(
		select={'num_cases':'malePatientCases + femalePatientCases'},
		order_by=['-num_cases'])
	if (len(worstZipcodes) > 0):
		data.worstZipcode = worstZipcodes[0].zipcode
	else:
		data.worstZipcode = 0

	# calculate numRecentCases
	lastmonth = datetime.datetime.now()
	if lastmonth.month > 1:
		lastmonth.replace(month = lastmonth.month - 1)
	else:
		lastmonth.replace(month = 12)
		lastmonth.replace(year = lastmonth.year - 1)
	data.numRecentCases = len(Message.objects.filter(state__exact=state, writtenDate__gt=lastmonth))
	
	# calculate percentIncrease
	lastlastmonth = datetime.datetime.now()
	if lastlastmonth.month > 1:
		lastlastmonth.replace(month = lastlastmonth.month - 1)
	else:
		lastlastmonth.replace(month = 12)
		lastlastmonth.replace(year = lastlastmonth.year - 1)
	lastmonthCases = len(Message.objects.filter(state__exact=state, writtenDate__gt=lastlastmonth)) - data.numRecentCases
	if lastmonthCases == 0:
		data.percentIncrease = 100
	else:
		data.percentIncrease = (data.numRecentCases - lastmonthCases)*100/lastmonthCases
	return [data]
