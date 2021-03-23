from django.contrib import admin

# Register your models here.
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('days', 'schedule')
    ordering = ('days', 'schedule')
    search_fields = ('days', 'schedule')

admin.site.register(Schedule, ScheduleAdmin)
