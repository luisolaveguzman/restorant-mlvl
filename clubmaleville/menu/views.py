from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import Carta, Category


class Carta(TemplateView):
    cartas = Carta.objects.order_by('id')
    categorys = Category.objects.order_by('id')
    template_name = "menu/menu.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['plats'] = self.cartas
        context['categorys'] = self.categorys
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
