from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('<int:id>', views.note, name='note'),
    path('new-note', views.new_note, name='new_note'),
    path('<int:id>/edit-note', views.edit_note, name='edit_note')
]
