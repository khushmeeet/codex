from django.urls import path
from . import views

urlpatterns = [
    path('new', views.save_webpage, name='save_webpage')
]