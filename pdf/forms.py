from django import forms


class ExternalDataPdfForm(forms.Form):
    pdf = forms.FileField()
