from django import template
from schedule.models import ROOMS

def filter_slot(value, arg):
	arg = int(arg)
	return [x for x in value if x.slot == arg]

def filter_room(value, arg):
	arg = int(arg)
	return [x for x in value if x.room == arg]

register = template.Library()

register.filter('filter_slot', filter_slot)
register.filter('filter_room', filter_room)