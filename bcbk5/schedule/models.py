from django.db import models
from django.core.exceptions import ValidationError

ROOMS = (
	(0, '17201'),
	(1, '17302'),
	(2, '17303'),
	(3, '17304'),
	(4, '17401'),
	(5, '17402'),
)
TIMESLOT = (
	(10, '10:40 - 11:10'),
	(20, '11:10 - 11:40'),
	(30, '11:40 - 12:10'),
	(40, '13:00 - 13:30'),
	(50, '13:30 - 14:00'),
	(60, '14:00 - 14:30'),
	(70, '14:30 - 15:00'),
	(80, '15:20 - 15:50'),
	(90, '15:50 - 16:20'),
	(100, '16:50 - 17:20'),
)

class Session(models.Model):
	name = models.CharField(max_length=255)
	by = models.CharField(max_length=255)
	room = models.SmallIntegerField(choices=ROOMS)
	slot = models.SmallIntegerField(choices=TIMESLOT)
	double = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	def get_time_start(self):
		return self.get_slot_display().split(' - ')[0]

	def get_time_end(self):
		if not self.double:
			return self.get_slot_display().split(' - ')[1]

		slot = [x[0] for x in TIMESLOT].index(self.slot)
		slot += 1

		return TIMESLOT[slot][1].split(' - ')[1]

	# def clean(self):
	# 	if self.double:
	# 		slot = [x[0] for x in TIMESLOT].index(self.slot)
	# 		if slot % 2 != 0:
	# 			raise ValidationError('Double sized session must fall on first of hour slot')

	class Meta:
		ordering = ['slot', 'room']