from django.contrib import admin

from .models import Carta, Category

class CartaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    ordering = ('name', 'category', 'price')
    search_fields = ('name', 'category__name', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition')
    search_fields = ('name', 'condition')

admin.site.register(Carta, CartaAdmin)
admin.site.register(Category, CategoryAdmin)