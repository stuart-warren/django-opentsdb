from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'dashboard.views.index'),
    url(r'^translate/nvd3\.json', 'dashboard.translate.nvd3'),

)
