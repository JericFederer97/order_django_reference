from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
from .models import Csv

#admin.site.register(Venue, VenueAdmin)
# admin.site.register(MyClubUser)
#admin.site.register(Event)
admin.site.register(Csv)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	ordering = ('name',)
	search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'event_date', 'description', 'manager')
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('event_date',)

