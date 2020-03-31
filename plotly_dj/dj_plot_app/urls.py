from django.urls import path
from . import views
# for some you need to import this if you dont watch it.
from .dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home_view, name = 'home') 
]
