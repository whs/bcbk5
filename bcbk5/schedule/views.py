from django.conf import settings
from django.views.generic import ListView

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from schedule.models import Session, ROOMS, TIMESLOT
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

class SessionRenderView(ListView):
	queryset = Session.objects.order_by('slot', 'room')
	template_name = 'schedule/timetable.html'
	context_object_name = 'sessions'

	def get_context_data(self, **kwargs):
		context = super(SessionRenderView, self).get_context_data(**kwargs)
		context['ROOMS'] = ROOMS
		context['TIMESLOT'] = TIMESLOT

		return context