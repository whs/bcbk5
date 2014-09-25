from django.conf.urls import patterns, include, url
from schedule.views import SessionView

urlpatterns = patterns('',
	url(r'^$', SessionView.as_view(), name='session')
)
