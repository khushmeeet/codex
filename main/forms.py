from django import forms
from .models import Notes


class NoteForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)
    entity = forms.CharField(label='Where is the note taken from?', required=True, max_length=500)
    source_type = forms.ChoiceField(label='What is the type of the source?', required=True, choices=Notes.SOURCE_TYPE_CHOICES)
    url = forms.URLField(label='URL of the source, if any', required=False)


