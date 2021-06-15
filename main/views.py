from django.http import HttpResponse
from django.shortcuts import render
from main.models import Notes
from main.forms import NoteForm


def notes_list(request):
    all_notes = Notes.objects.all()
    context = {
        'all_notes': all_notes
    }
    return render(request, 'home.html', context)


def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            return HttpResponse('Got the form values')
    else:
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'home.html', context)
