import json

from django.core.exceptions import ValidationError
from rest_framework import serializers

from registration.models import Registration

class InterestField(serializers.WritableField):
	def to_native(self, obj):
		return json.loads(obj)

	def from_native(self, data):
		# empty input
		if not data:
			return '[]'

		# json input
		if type(data) == list:
			data = self.clean_data(data)
			return json.dumps(data)

		# string input
		try:
			out = json.loads(data)
			if type([]) != list:
				raise ValidationError('Data is not array')
			out = self.clean_data(out)
			return json.dumps(out)
		except ValueError:
			raise ValidationError('Data must be in JSON array')

	def clean_data(self, out):
		return [x[:40] for x in out[:10]]

class RegistrationSerializer(serializers.ModelSerializer):
	interests = InterestField(required=False)

	class Meta:
		model = Registration
		fields = (
			'id', 'name', 'profession', 'work', 'twitter', 'web',
			'interests', 'shirt', 'food'
		)