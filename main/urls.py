from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('note/<int:id>', views.view_note, name='view_note'),
    path('note/<int:id>/edit', views.edit_note, name='edit_note'),
    path('new-note', views.new_note, name='new_note'),
]
