from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from schedule.models import Session
from schedule.serializers import SessionSerializer

class SessionView(generics.ListAPIView):
	"""
	List sessions.

	room -- tbd
	slot -- tbd
	double -- true for 1 hr session length
	"""
	queryset = Session.objects.all()
	serializer_class = SessionSerializer