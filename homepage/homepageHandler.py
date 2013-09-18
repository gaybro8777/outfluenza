from zipcodes.models import Zipcode
from message.models import Message
from django.db.models import Sum
from homepage.models import State

TOTAL_BUCKETS = 10

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

def orderZipcodesFromState(state):
	return Zipcode.objects.filter(state__exact = state)

def orderMessagesIntoSortedStates():
	messages = Message.objects.values('state')
	print(messages)