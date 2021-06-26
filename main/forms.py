from django import forms
from .models import Notes


class NoteForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)
    entity = forms.CharField(label='entity', required=True, max_length=500)
    source_type = forms.ChoiceField(label='source_type', required=True, choices=Notes.SOURCE_TYPE_CHOICES)
    url = forms.URLField(label='url', required=False)


class TagForm(forms.Form):
    tag = forms.CharField(label='Tag', required=True)


