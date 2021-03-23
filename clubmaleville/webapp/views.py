from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from slide.models import Slide
from schedule.models import Schedule
from contact.models import Contact
from contact.forms import NewsletterForm


class Home(TemplateView):
    #model = Slide
    slide = Slide.objects.order_by('id')

    template_name = "webapp/home.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['slides'] = self.slide

        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

