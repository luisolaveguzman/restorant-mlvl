from django.contrib import admin

# Register your models here.
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'date', 'hour', 'cant', 'state')
    search_fields = ('name', 'mail', 'phone', 'date', 'hour', 'cant', 'state')

admin.site.register(Reservation, ReservationAdmin)