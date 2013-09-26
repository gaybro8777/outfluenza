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
    url(r'^statesjson/$', homepage.views.StatesJson),
    url(r'^ustimegraphjson/$', homepage.views.USTimeGraph),
    url(r'^statesstatisticjson/$', homepage.views.StatesStatisticJson),
    url(r'^zipcodesjson/(?P<state>[A-Z]{2})$', homepage.views.ZipcodesJson),
    url(r'^messagesjson/', homepage.views.MessagesJson),

    # Search Requests
    url(r'^findZipcode/(?P<zipcode>[0-9]+)$', homepage.views.ZipcodeSearch),
    url(r'^findState/(?P<state>[A-Z|a-z]+)$', homepage.views.StateSearch),    

    # Homepage
    url(r'^$', homepage.views.HomepageView, name = 'homepage'),
    url(r'^state/(?P<state>[A-Z]{2})$', homepage.views.StateView, name = 'stateView'),
    url(r'^team/$', homepage.views.TeamView),
    url(r'^instructions/$', homepage.views.InstructionsView),

    # Default
    # url(r'[.]*', homepage.views.DefaultRedirect, name = 'homepage'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )