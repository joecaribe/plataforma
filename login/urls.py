from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('conta/', include('django.contrib.auth.urls') ),
]