from django.urls import path
from .views import Carta


carta_patterns = ([
    path('', Carta.as_view(), name="carta"),
], 'carta')