from django.contrib import admin

from .models import MenuDiario, Entrada, Acompanamiento, Especialidades


class MenuDiarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition')
    search_fields = ('name', 'condition')

class AcompanamientoAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition')
    search_fields = ('name', 'condition')

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'condition')
    search_fields = ('name', 'price', 'condition')

admin.site.register(MenuDiario, MenuDiarioAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Acompanamiento, AcompanamientoAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)

