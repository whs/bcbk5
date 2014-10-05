from rest_framework import serializers

from schedule.models import Session

class SessionSerializer(serializers.ModelSerializer):
	room = serializers.SerializerMethodField('get_room_display')
	slot = serializers.SerializerMethodField('get_slot_display')
	class Meta:
		model = Session
		fields = (
			'id', 'name', 'room', 'by', 'slot', 'double'
		)

	def get_room_display(self, obj):
		return obj.get_room_display()

	def get_slot_display(self, obj):
		return obj.get_slot_display()
