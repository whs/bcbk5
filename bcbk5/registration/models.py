import json
import re

from django.core.exceptions import ValidationError
from django.db import models

SHIRT_SIZES = (
	(0, 'S'),
	(1, 'M'),
	(2, 'L'),
	(3, 'XL'),
	(4, 'XXL')
)

FOOD_PREF = (
	(0, 'Normal'),
	(1, 'Halal'),
	(2, 'Vegetarian')
)

class Registration(models.Model):
	name = models.CharField(max_length=255, unique=True)
	profession = models.CharField(max_length=255, blank=True)
	work = models.CharField(max_length=255, blank=True)
	twitter = models.CharField(max_length=15, blank=True)
	web = models.URLField(blank=True)
	interests = models.CharField(max_length=255, blank=True)
	shirt = models.SmallIntegerField(default=1, choices=SHIRT_SIZES)
	food = models.SmallIntegerField(default=0, choices=FOOD_PREF)
	created = models.DateTimeField(auto_now=True)

	def clean(self):
		if self.twitter.startswith("@"):
			self.twitter = self.twitter[1:]
		if self.twitter and not re.match(r'^[a-zA-Z0-9]+$', self.twitter):
			raise ValidationError('Invalid Twitter username')
		if self.interests:
			try:
				assert type(json.loads(self.interests)) == list
			except (ValueError, AssertionError):
				raise ValidationError('Interest must be JSON list')

	def __unicode__(self):
		return self.name
