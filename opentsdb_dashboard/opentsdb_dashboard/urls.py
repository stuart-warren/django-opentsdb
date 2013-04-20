from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opentsdb_dashboard.views.home', name='home'),
    # url(r'^opentsdb_dashboard/', include('opentsdb_dashboard.foo.urls')),

    # Redirect straight to /dashboard
    url(r'^$', lambda x: HttpResponseRedirect('/dashboard/')),
    url(r'^dashboard/', include('dashboard.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
