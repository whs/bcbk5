import urllib

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.renderers import JSONRenderer

from schedule.models import Session
from schedule.serializers import SessionSerializer

raven = None

try:
	from raven.contrib.django.raven_compat.models import client as raven
except ImportError:
	pass

@receiver(post_save)
def db_save(sender, instance, created, **kwargs):
	if settings.PUSH_PUBLISH and sender == Session:
		try:
			urllib.urlopen(
				settings.PUSH_PUBLISH,
				JSONRenderer().render(SessionSerializer(instance).data)
			)
		except IOError:
			if raven:
				raven.captureException()
