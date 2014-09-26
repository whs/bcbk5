from django.conf.urls import patterns, include, url
from schedule.views import SessionView, SessionRenderView

urlpatterns = patterns('',
	url(r'^$', SessionView.as_view(), name='session'),
	url(r'^render$', SessionRenderView.as_view(), name='session_table')
)
