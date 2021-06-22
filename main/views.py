from django.shortcuts import render, redirect, get_object_or_404
from main.models import Notes
from main.forms import NoteForm
import markdown
from markdownify import markdownify as md
import datetime

html = markdown.Markdown(extensions=['extra', 'codehilite', 'nl2br', 'sane_lists', 'smarty'])


def notes_list(request):
    all_notes = Notes.objects.all()
    context = {
        'all_notes': all_notes
    }
    return render(request, 'home.html', context)


def view_note(request, id):
    note = get_object_or_404(Notes, id=id)
    context = {
        'note': note
    }
    return render(request, 'view-note.html', context)


def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Notes(
                content=html.convert(form.cleaned_data['content']),
                entity=form.cleaned_data['entity'],
                url=form.cleaned_data['url'],
                added_on=datetime.datetime.now(datetime.timezone.utc),
                last_modified_on=datetime.datetime.now(datetime.timezone.utc),
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


def edit_note(request, id):
    note = get_object_or_404(Notes, id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note.content = html.convert(form.cleaned_data['content'])
            note.entity = form.cleaned_data['entity']
            note.url = form.cleaned_data['url']
            note.source_type = form.cleaned_data['source_type']
            note.last_modified_on = datetime.datetime.now(datetime.timezone.utc)
            note.save()
            return redirect('notes_list')
    else:
        note_data = {
            'content': md(note.content, heading_style='ATX'),
            'entity': note.entity,
            'source_type': note.source_type,
            'url': note.url
        }
        nf = NoteForm(note_data)
        context = {
            'form': nf,
            'id': note.id
        }
        return render(request, 'edit-note.html', context)
