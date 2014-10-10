from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders

from registration.models import Registration

@receiver(post_save)
def db_save(sender, instance, created, **kwargs):
	if sender == Registration and created and instance.email:
		email = EmailMultiAlternatives(
			'Barcamp Bangkhen 2014 Registration Confirmation',
			render_to_string('registration/email_regis.txt', {'regis': instance}),
			settings.DEFAULT_FROM_EMAIL,
			['{0} <{1}>'.format(instance.name, instance.email)],
		)
		email.attach_file(finders.find('barcamp.ics'))
		email.attach_alternative(render_to_string('registration/email_regis.html', {'regis': instance}), 'text/html')
		email.send(True)