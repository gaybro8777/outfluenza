from django.http import HttpResponse
from django.template import RequestContext, loader
from zipcodes.models import Zipcode
import json
from django.core import serializers
from homepage.homepageHandler import orderZipcodesIntoSortedStates, orderZipcodesFromState

def HomepageView(request):
    template = loader.get_template('homepage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def ZipcodesJson(request, state):
	state = orderZipcodesFromState(state)
	return HttpResponse(serializers.serialize("json", state, ensure_ascii=False))

def StatesJson(request):
	states = orderZipcodesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", states, ensure_ascii=False))
