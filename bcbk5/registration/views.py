from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from registration.models import Registration
from registration.serializers import RegistrationSerializer

class RegistrationView(generics.ListCreateAPIView):
	"""
	List and create registration. The creation is rate limited to 1 per minute.

	twitter -- Prefix @ is filtered out automatically
	interests -- Must be either empty or JSON array
	food -- Must be one of 0=Normal 1=Halal 2=Vegetarian
	shirt -- Must be one of 0=S 1=M 2=L 3=XL 4=XXL
	"""
	queryset = Registration.objects.all()
	serializer_class = RegistrationSerializer
	throttle_scope = 'regis'

	def create(self, request, *args, **kwargs):
		if not settings.REGIS_OPEN:
			return Response({
				'__all__': ['Registration is closed']
			}, status=status.HTTP_403_FORBIDDEN)

		return super(generics.ListCreateAPIView, self).create(request, *args, **kwargs)
