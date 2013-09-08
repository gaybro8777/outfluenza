from django.http import HttpResponse
from django.template import RequestContext, loader


def HomepageView(request):
    template = loader.get_template('homepage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
