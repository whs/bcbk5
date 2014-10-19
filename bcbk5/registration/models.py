# encoding: utf-8
import json
import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html

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
	shirt = models.SmallIntegerField("Shirt size", default=1, choices=SHIRT_SIZES)
	food = models.SmallIntegerField("Food preference", default=0, choices=FOOD_PREF)
	food_allergic = models.CharField("Food allergic", default="", max_length=255, blank=True)
	email = models.EmailField(blank=True)
	created = models.DateTimeField(auto_now=True)

	def twitter_link(self):
		if not self.twitter:
			return ''
		return format_html('@<a href="https://twitter.com/{0}" target="_blank">{0}</a>', self.twitter)
	twitter_link.admin_order_field = 'twitter'

	def web_link(self):
		if not self.web:
			return ''
		return format_html('<a href="{0}" target="_blank">{0}</a>', self.web)
	web_link.admin_order_field = 'web'

	def clean(self):
		if self.twitter.startswith("@"):
			self.twitter = self.twitter[1:]
		if self.twitter and not re.match(r'^[a-zA-Z0-9_]{1,15}$', self.twitter):
			raise ValidationError('Invalid Twitter username')

	def dictionary_first_char(self):
		if self.name[0] in u'เแโไใ':
			return self.name[1].upper()
		return self.name[0].upper()

	def __unicode__(self):
		return self.name
