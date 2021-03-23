from django.urls import path
from .views import CreateReservation

reservas_patterns = ([
    path('', CreateReservation.as_view(), name="reservas"),
], 'reservas')