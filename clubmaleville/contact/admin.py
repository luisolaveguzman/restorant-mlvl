from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail')
    ordering = ('name', 'mail')
    search_fields = ('name', 'mail')

admin.site.register(Contact, ContactAdmin)