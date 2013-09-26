from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from zipcodes.models import Zipcode
from message.models import Message
from homepage.models import USTimeGraphJson
from uploadXML.zipcodes_to_state import zipcodes_to_state
from uploadXML.state_finder import state_finder
import json
from django.core import serializers
from django.db.models import Count
from outfluenza.settings import STATIC_URL
from homepage.homepageHandler import orderZipcodesIntoSortedStates, orderZipcodesFromState, orderMessagesIntoSortedStates

################################
# Views

def HomepageView(request):
    template = loader.get_template('homepage.html')
    context = RequestContext(request)
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
		return HttpResponseRedirect("/state/" + result);
	else:
		return HttpResponseRedirect("/")

def StateSearch(request, state):
	result = state_finder[state.lower()];
	if result:
		return HttpResponseRedirect("/state/" + result);
	else:
		return HttpResponseRedirect("/")

################################
# Data

def ZipcodesJson(request, state):
	state = orderZipcodesFromState(state)
	return HttpResponse(serializers.serialize("json", state, ensure_ascii=False))

def StatesJson(request):
	states = orderZipcodesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", states, ensure_ascii=False))

def StatesStatisticJson(request):
	messages = orderMessagesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))	

def USTimeGraph(request):
	messages = Message.objects.values('writtenDate').annotate(num = Count('writtenDate')).order_by('writtenDate')
	messages = [USTimeGraphJson().populate(m['writtenDate'], m['num']) for m in messages]
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))

def MessagesJson(request):
	messages = Message.objects.all()
	return HttpResponse(serializers.serialize("json", messages, ensure_ascii=False))

################################
# Redirect

def DefaultRedirect(request):
	return HttpResponseRedirect("/")
