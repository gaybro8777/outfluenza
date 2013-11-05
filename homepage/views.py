from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from zipcodes.models import Zipcode
from message.models import Message
from age.models import Age
from homepage.models import USTimeGraphJson
from uploadXML.zipcodes_to_state import zipcodes_to_state
from uploadXML.state_finder import state_finder
import json
import string
from django.core import serializers
from django.db.models import Count
from outfluenza.settings import STATIC_URL
from homepage.homepageHandler import orderZipcodesIntoSortedStates, \
	orderCountiesFromState, orderMessagesIntoSortedStates, getTopZipcodes, \
	getTopDrug, orderGenderFromState, orderAgeFromState, orderMessagesIntoState, \
	getTopMetrics, predictBuckets

################################
# Views

def HomepageView(request):
    template = loader.get_template('homepage.html')
    context = RequestContext(request, {'topDrug': getTopDrug()})
    return HttpResponse(template.render(context))

def StateView(request, state):
	template = loader.get_template('state.html')
	context = RequestContext(request, {'state':state})
	return HttpResponse(template.render(context))

def TeamView(request):
	template = loader.get_template('team.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def InstructionsView(request):
	template = loader.get_template('instructions.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

################################
# Search

def ZipcodeSearch(request, zipcode):
	zippie = int(zipcode)
	result = zipcodes_to_state[zippie];
	if result:
		return HttpResponse(result);
	else:
		return HttpResponseRedirect("/findState/" + zipcode)

def StateSearch(request, state):
	result = state_finder[string.replace(state.lower(), "%20", " ")];
	if result:
		return HttpResponse(serializers.serialize("json", {'state':result}, ensure_ascii=False));
	else:
		return HttpResponseRedirect("/")

def Search(request, query):
	return HttpResponseRedirect("/")

################################
# Data

def CountyJson(request, state):
	state = orderCountiesFromState(state)
	return HttpResponse(serializers.serialize("json", state, ensure_ascii=False))

def StatesJson(request):
	states = orderZipcodesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", states, ensure_ascii=False))

def Prediction(request, num):
	states = orderZipcodesIntoSortedStates()
	for i in range(int(num)):
		predictBuckets(states)
	return HttpResponse(serializers.serialize("json", states, ensure_ascii=False))

def StatesStatisticJson(request):
	messages = orderMessagesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))	

def USTimeGraph(request):
	messages = Message.objects.values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	messages = [USTimeGraphJson().populate(m['writtenDate'], m['num']) for m in messages]
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))

def TopZipcodesJson(request):
	zipcodes = getTopZipcodes()
	return HttpResponse(serializers.serialize("json", zipcodes, ensure_ascii=False))

def GenderJson(request, state):
	gender = orderGenderFromState(state)
	return HttpResponse(serializers.serialize("json", [gender], ensure_ascii=False))

def AgeJson(request, state):
	ages = orderAgeFromState(state)
	return HttpResponse(serializers.serialize("json", ages, ensure_ascii=False))	

def StateTimeGraph(request, state):
	messages = orderMessagesIntoState(state)
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))

def TopMetrics(request, state):
	data = getTopMetrics(state)
	return HttpResponse(serializers.serialize("json", data, ensure_ascii=False))	

################################
# Redirect

def DefaultRedirect(request):
	return HttpResponseRedirect("/")
