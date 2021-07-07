from django import forms
from .models import ExternalData


class ExternalDataForm(forms.Form):
    url = forms.URLField(label='url', required=True)