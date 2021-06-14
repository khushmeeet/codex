from django.shortcuts import render
from main.models import Notes


def index(request):
    all_notes = Notes.objects.all()
    context = {
        'all_notes': all_notes
    }
    return render(request, 'home.html', context)
