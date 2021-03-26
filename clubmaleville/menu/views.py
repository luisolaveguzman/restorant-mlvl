from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import Carta, Category


class Carta(TemplateView):
    carta = Carta.objects.all()
    categorys = Category.objects.all()
    template_name = "menu/menu.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['plats'] = self.carta
        context['categorys'] = self.categorys
        return context

    def get(self, request, *args, **kwargs):
        print(self.carta)
        return render(request, self.template_name, self.get_context_data())
