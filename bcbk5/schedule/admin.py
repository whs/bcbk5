from django.contrib import admin
from schedule.models import Session

class SessionAdmin(admin.ModelAdmin):
	list_display = ('name', 'by', 'room', 'slot', 'double')
	list_editable = ('room', 'slot')
	list_filter = ('room', 'slot')
	search_fields = ['name', 'by']

admin.site.register(Session, SessionAdmin)