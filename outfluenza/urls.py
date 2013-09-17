from django.conf.urls import patterns, include, url
import messages.views
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

    url(r'^messages/$', messages.views.ListMessageView, name = 'messages-list',),
    url(r'^upload/$', uploadXML.views.UploadFileView, name = 'uploadxml'),
    url(r'^zipcodes/$', zipcodes.views.ListZipcodeView, name = 'zipcodes-list'),
    url(r'^zipcodesjson/$', homepage.views.ZipcodesJson, name = 'zipcodesjson'),
    url(r'^$', homepage.views.HomepageView, name = 'homepage'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )