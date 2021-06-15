from django.http import HttpResponse
from django.shortcuts import render, redirect
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
            note = Notes(
                content=form.cleaned_data['content'],
                source=form.cleaned_data['source'],
                url=form.cleaned_data['url'],
                added_on=form.cleaned_data['added_on'],
                source_type=form.cleaned_data['source_type']
            )
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'new-note.html', context)
