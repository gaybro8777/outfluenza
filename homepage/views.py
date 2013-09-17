from django.http import HttpResponse
from django.template import RequestContext, loader
from zipcodes.models import Zipcode
import json
from django.core import serializers
from zipcodes.zipcodeHandler import orderZipcodesIntoSortedStates

def HomepageView(request):
    template = loader.get_template('homepage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def ZipcodesJson(request):
	states = orderZipcodesIntoSortedStates()
	return HttpResponse(serializers.serialize("json", states, ensure_ascii=False))
