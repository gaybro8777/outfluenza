from zipcodes.models import Zipcode
from message.models import Message
from django.db.models import Sum, Count
from homepage.models import State

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
		.annotate(num_male_cases=Sum('malePatientCases'), num_female_cases=Sum('femalePatientCases')) \
		.order_by('-num_male_cases')
	assignBuckets(states)
	states = [State().populate(s['state'], s['num_male_cases'], s['bucket']) for s in states]
	return states

def orderZipcodesFromState(state):
	return Zipcode.objects.filter(state__exact = state)

def orderMessagesIntoSortedStates():
	messages = Message.objects.values('state')
	print(messages)

def getTopZipcodes():
	return Zipcode.objects.order_by('-malePatientCases')[:5]

def getTopDrug():
	product = Message.objects.values('productCode').annotate(num=Count('productCode')).order_by('-num')[0:5]
	return product[0]['productCode']