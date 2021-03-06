from django.urls import path
from .views import Home


webapp_patterns = ([
    path('', Home.as_view(), name="home"),
], 'webapp')