from django.conf.urls import patterns, include, url
from django.views.decorators.clickjacking import xframe_options_exempt

from schedule.views import SessionView, SessionRenderView

urlpatterns = patterns('',
	url(r'^$', SessionView.as_view(), name='session'),
	url(r'^render$', xframe_options_exempt(SessionRenderView.as_view()), name='session_table')
)
