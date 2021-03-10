from django.urls import path
from .views import Menu


menudiario_patterns = ([
    path('', Menu.as_view(), name="menu"),
], 'menudiario')