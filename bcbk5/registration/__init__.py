from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string

from registration.models import Registration

@receiver(post_save)
def db_save(sender, instance, created, **kwargs):
	if sender == Registration and created and instance.email:
		send_mail(
			'Barcamp Bangkhen 5 Registration',
			render_to_string('registration/email_regis.txt', {'regis': instance}),
			settings.DEFAULT_FROM_EMAIL,
			[instance.email],
			True,
			html_message=render_to_string('registration/email_regis.html', {'regis': instance})
		)