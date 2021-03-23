"""clubmaleville URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from webapp.urls import webapp_patterns
from menu.urls import carta_patterns
from menudiario.ursl import menudiario_patterns
from reservas.urls import reservas_patterns
from contact.urls import contact_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(webapp_patterns)),
    path('carta/', include(carta_patterns)),
    path('menu/', include(menudiario_patterns)),
    path('reservas/', include(reservas_patterns)),
    path('contacto/', include(contact_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)