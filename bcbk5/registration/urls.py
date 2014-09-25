from django.conf.urls import patterns, include, url
from registration.views import RegistrationView

urlpatterns = patterns('',
	url(r'^$', RegistrationView.as_view(), name='registration')
)
