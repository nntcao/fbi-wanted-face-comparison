import django
from django.http import HttpResponse


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/hello', views.index),
]
