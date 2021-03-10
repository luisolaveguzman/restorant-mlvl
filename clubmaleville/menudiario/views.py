from django.shortcuts import render
from django.views.generic import TemplateView

from .models import MenuDiario, Entrada, Acompanamiento, Especialidades


class Menu(TemplateView):
    menu = MenuDiario.objects.order_by('id')
    entrada = Entrada.objects.order_by('id')
    acompanamiento = Acompanamiento.objects.order_by('id')
    especialidades = Especialidades.objects.order_by('id')
    template_name = "menudiario/menudiario.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['menus'] = self.menu
        context['entradas'] = self.entrada
        context['acompanamientos'] = self.acompanamiento
        context['especialidades'] = self.especialidades
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())