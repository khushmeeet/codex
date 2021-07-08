from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_pdfs, name='list_pdfs'),
    path('new', views.save_pdf, name='save_pdf'),
    path('view/<int:id>', views.view_pdf, name='view_pdf')
]