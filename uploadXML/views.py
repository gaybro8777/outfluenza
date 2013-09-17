from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import CreateView

from uploadXML.models import UploadFileForm
from uploadXML.uploadHandler import handleUpload

def UploadFileView(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		handleUpload(request.FILES['file'])
		return HttpResponseRedirect('/zipcodes')
	template = loader.get_template('upload_file.html')
	context = RequestContext(request, {
			'form' : UploadFileForm(),
		})
	return HttpResponse(template.render(context))
