from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_webpages, name='list_webpages'),
    path('new', views.save_webpage, name='save_webpage')
]