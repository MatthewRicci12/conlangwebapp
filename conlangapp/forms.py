from django import forms
from .models import *

class SubmitTextForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Text
        fields = ['title', 'body']
        exclude = ['date_added']

class UploadFileForm(forms.Form):
    file = forms.FileField()