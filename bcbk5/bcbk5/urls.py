from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^regis/', include('registration.urls')),
    url(r'^session/', include('schedule.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('rest_framework_docs.urls'))
)
