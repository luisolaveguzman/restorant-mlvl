from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreateReservationForm
from .models import Reservation


class CreateReservation(CreateView):
    model = Reservation
    form_class = CreateReservationForm
    template_name = 'reservas/reservation.html'
    success_url = reverse_lazy('carta:carta')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            reserva = Reservation(
                name=form.cleaned_data.get('name'),
                mail = form.cleaned_data.get('mail'),
                phone = form.cleaned_data.get('phone'),
                date = form.cleaned_data.get('date'),
                hour = form.cleaned_data.get('hour'),
                cant = form.cleaned_data.get('cant'),
                detail = form.cleaned_data.get('detail')
            )
            fecha = reserva.date
            reserva.date = fecha
            reserva.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form':form})