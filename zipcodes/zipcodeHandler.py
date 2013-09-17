from django.db.models import Sum
from messages.models import Message
from zipcodes.models import Zipcode
from zipcodes.models import State
from django.utils import simplejson

TOTAL_BUCKETS = 10

def handleZipcode(message):
	print(message)
	if message.prescriberZipcode:
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.prescriberZipcode)
		if len(zipcodes) > 0:
			zipcodes[0].prescriberCases += 1
			zipcodes[0].save()
		else:
			new_zipcode = Zipcode().defaultFields(message.prescriberZipcode)			
			print(new_zipcode)
			new_zipcode.prescriberCases += 1
			new_zipcode.save()

	if message.patientZipcode:
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.patientZipcode)
		if len(zipcodes) > 0:
			zipcodes[0].patientCases += 1
			zipcodes[0].save()
		else:
			new_zipcode = Zipcode().defaultFields(message.patientZipcode)
			new_zipcode.patientCases += 1
			new_zipcode.save()

	if message.pharmacyZipcode:
		zipcodes = Zipcode.objects.filter(zipcode__exact = message.pharmacyZipcode)
		if len(zipcodes) > 0:
			zipcodes[0].pharmacyCases += 1
			zipcodes[0].save()
		else:
			new_zipcode = Zipcode().defaultFields(message.pharmacyZipcode)
			new_zipcode.pharmacyCases += 1
			new_zipcode.save()

def assignBuckets(states):
	num_states = len(states)
	per_bucket = 1.0
	if (num_states > TOTAL_BUCKETS):
		per_bucket = float(num_states) / float(TOTAL_BUCKETS)
	curr_bucket = 0
	counter = 0
	for s in states:
		s['bucket'] = curr_bucket
		counter += 1
		if counter >= per_bucket:
			counter = 0
			curr_bucket += 1


def orderZipcodesIntoSortedStates():
	states = Zipcode.objects.values('state').annotate(num_cases=Sum('patientCases')).order_by('num_cases')
	assignBuckets(states)
	states = [State().populate(s['state'], s['num_cases'], s['bucket']) for s in states]
	return states
