from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_weblink, name='new_weblink')
]