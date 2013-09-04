from django.http import HttpResponse
from django.template import RequestContext, loader
from messages.models import Message


def ListMessageView(request):
    template = loader.get_template('message_list.html')
    allMessages = Message.objects.filter()
    context = RequestContext(request, {
    	'allMessages': allMessages,
    })
    return HttpResponse(template.render(context))