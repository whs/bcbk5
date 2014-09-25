import json

from django.core.exceptions import ValidationError
from rest_framework import serializers

from registration.models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registration
		fields = (
			'id', 'name', 'profession', 'work', 'twitter', 'web',
			'interests', 'shirt', 'food', 'email'
		)
		write_only_fields = ('shirt', 'food', 'email')