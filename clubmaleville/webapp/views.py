from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from slide.models import Slide

class Home(TemplateView):
    model = Slide
    template_name = "webapp/home.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['slides'] = self.model.objects.order_by('id')
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

