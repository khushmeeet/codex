from django.shortcuts import render, redirect, get_object_or_404
from main.models import Notes
from main.forms import NoteForm
import markdown
import datetime


def notes_list(request):
    all_notes = Notes.objects.all()
    for n in all_notes:
        if len(n.content) > 250:
            n.content = n.content[:250] + '...'
    context = {
        'all_notes': all_notes
    }
    return render(request, 'home.html', context)


def note(request, id):
    note = get_object_or_404(Notes, id=id)
    context = {
        'note': note
    }
    return render(request, 'home.html', context=context)


def new_note(request):
    if request.method == 'POST':
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'nl2br', 'sane_lists', 'smarty'])
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Notes(
                content=md.convert(form.cleaned_data['content']),
                entity=form.cleaned_data['entity'],
                url=form.cleaned_data['url'],
                added_on=datetime.datetime.now(datetime.timezone.utc),
                source_type=form.cleaned_data['source_type']
            )
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
        context = {
            'form': form
        }
        return render(request, 'note.html', context)


def edit_note(request, id):
    note = get_object_or_404(Notes, id=id)
    if request.method == 'PUT':
        form = NoteForm(request.PUT)
        note.content = form.cleaned_data['content']
        note.entity = form.cleaned_data['entity'],
        note.url = form.cleaned_data['url'],
        note.added_on = form.cleaned_data['added_on'],
        note.source_type = form.cleaned_data['source_type']
        note.save()
        redirect('notes_list')
    else:
        context = {
            'note': note
        }
        return render(request, 'note.html', context)
