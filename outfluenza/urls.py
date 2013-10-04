from django.conf.urls import patterns, include, url
import message.views
import uploadXML.views
import zipcodes.views
import homepage.views
import settings
import predictions.views
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
    url(r'^statetimegraphjson/(?P<state>[A-Z]{2})$', homepage.views.StateTimeGraph),
    url(r'^statesstatisticjson/$', homepage.views.StatesStatisticJson),
    url(r'^countyjson/(?P<state>[A-Z]{2})$', homepage.views.CountyJson),
    url(r'^topzipcodesjson/$', homepage.views.TopZipcodesJson),
    url(r'^genderjson/(?P<state>[A-Z]{2})$', homepage.views.GenderJson),
    url(r'^agejson/(?P<state>[A-Z]{2})$', homepage.views.AgeJson),
    url(r'^topmetrics/(?P<state>[A-Z]{2})$', homepage.views.TopMetrics),

    # Search Requests
    url(r'^find/(?P<zipcode>[0-9]+)$', homepage.views.ZipcodeSearch),
    url(r'^find/(?P<state>[A-Z|a-z|\w|\W]+)$', homepage.views.StateSearch),    
    url(r'^find/(?P<query>.+)$', homepage.views.Search),

    # Homepage
    url(r'^$', homepage.views.HomepageView, name = 'homepage'),
    url(r'^state/(?P<state>[A-Z]{2})$', homepage.views.StateView, name = 'stateView'),
    url(r'^team/$', homepage.views.TeamView),
    url(r'^instructions/$', homepage.views.InstructionsView),

    # Predictions
    url(r'^createpredictions/$', predictions.views.CreatePredictions),    

    # Default
    # url(r'[.]*', homepage.views.DefaultRedirect, name = 'homepage'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )