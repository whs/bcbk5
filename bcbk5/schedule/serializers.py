from rest_framework import serializers

from schedule.models import Session

class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = (
			'id', 'name', 'by', 'room', 'slot', 'double'
		)