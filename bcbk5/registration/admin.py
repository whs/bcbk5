from django.contrib import admin
from django.shortcuts import render_to_response

from registration.models import Registration

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('name', 'twitter_link', 'web_link', 'food', 'shirt', 'created')
	list_filter = ('shirt', 'food')
	search_fields = ['name', 'profession', 'work']

	actions = ['printable']

	def printable(self, request, queryset):
		# name field must use tis620_thai_ci
		# http://bugs.mysql.com/bug.php?id=32183
		query = Registration.objects.extra(select={'name_lower': 'lower(name)'})
		query = query.order_by('name_lower')
		return render_to_response('registration/print.html', {
			'regis': query
		})

	printable.short_description = 'Printable list of all registration'

admin.site.register(Registration, RegistrationAdmin)