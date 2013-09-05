from django.http import HttpResponse
from django.template import RequestContext, loader
from zipcodes.models import Zipcode


def ListZipcodeView(request):
    template = loader.get_template('zipcode_list.html')
    allZipcodes = Zipcode.objects.filter()
    context = RequestContext(request, {
    	'allZipcodes': allZipcodes,
    })
    return HttpResponse(template.render(context))