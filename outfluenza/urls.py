from django.conf.urls import patterns, include, url
import message.views
import uploadXML.views
import zipcodes.views
import homepage.views
import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'outfluenza.views.home', name='home'),
    # url(r'^outfluenza/', include('outfluenza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # List Requests
    url(r'^messages/$', message.views.ListMessageView, name = 'messages-list',),
    url(r'^upload/$', uploadXML.views.UploadFileView, name = 'uploadxml'),
    url(r'^zipcodes/$', zipcodes.views.ListZipcodeView, name = 'zipcodes-list'),

    # Data Requests
    url(r'^statesjson/$', homepage.views.StatesJson, name = 'statesjson'),
    url(r'^ustimegraphjson/$', homepage.views.USTimeGraph, name = 'USTimeGraphJson'),
    url(r'^statesstatisticjson/$', homepage.views.StatesStatisticJson, name = 'statesStatisticJson'),
    url(r'^zipcodesjson/(?P<state>[A-Z]{2})$', homepage.views.ZipcodesJson, name = 'zipcodesjson'),

    # Homepage
    url(r'^$', homepage.views.HomepageView, name = 'homepage'),
    url(r'^state/(?P<state>[A-Z]{2})$', homepage.views.StateView, name = 'stateView'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )