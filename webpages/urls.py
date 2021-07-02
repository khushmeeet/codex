from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_webpages, name='list_webpages'),
    path('new', views.save_webpage, name='save_webpage'),
    path('view/<int:id>', views.view_webpage, name='view_webpage'),
    path('note/<int:id>/delete', views.delete_webpage, name='delete_webpage')
]