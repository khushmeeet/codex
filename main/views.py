from django.shortcuts import render, redirect, get_object_or_404
from main.models import Notes, Tags
from main.forms import NoteForm, TagForm
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
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            tag = Tags(tag=request.POST['tag'].lower())
            tag.save()
            note = Notes(
                content=html.convert(note_form.cleaned_data['content']),
                entity=note_form.cleaned_data['entity'],
                url=note_form.cleaned_data['url'],
                tag=tag,
                added_on=datetime.datetime.now(datetime.timezone.utc),
                last_modified_on=datetime.datetime.now(datetime.timezone.utc),
                source_type=note_form.cleaned_data['source_type']
            )
            note.save()
            return redirect('notes_list')
    else:
        note_form = NoteForm()
        tag_form = TagForm()
        context = {
            'note_form': note_form,
            'tag_form': tag_form
        }
        return render(request, 'new-note.html', context)


def edit_note(request, id):
    note = get_object_or_404(Notes, id=id)
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            tag, _ = Tags.objects.get_or_create(tag=request.POST['tag'].lower())
            note.content = html.convert(note_form.cleaned_data['content'])
            note.entity = note_form.cleaned_data['entity']
            note.url = note_form.cleaned_data['url']
            note.tag = tag
            note.source_type = note_form.cleaned_data['source_type']
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
        tag_data = {
            'tag': note.tag.tag
        }
        nf = NoteForm(note_data)
        tf = TagForm(tag_data)
        context = {
            'note_form': nf,
            'tag_form': tf,
            'id': note.id
        }
        return render(request, 'edit-note.html', context)


def delete_note(request, id):
    Notes.objects.filter(id=id).delete()
    return redirect('notes_list')
