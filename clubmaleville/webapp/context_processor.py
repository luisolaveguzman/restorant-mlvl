from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from contact.forms import NewsletterForm

from schedule.models import Schedule


def context_extend(request):
    context = {}
    schedule = Schedule.objects.order_by('id')
    context['schedules'] = schedule
    return context