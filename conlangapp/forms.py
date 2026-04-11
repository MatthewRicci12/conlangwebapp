from django import forms
from django.forms import ChoiceField
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

class VocabularyEntryForm(forms.ModelForm):
    part_of_speech = ChoiceField(choices=VocabularyEntry.PartOfSpeech)
    definition = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = VocabularyEntry
        fields = ['part_of_speech', 'definition']

class GlyphForm(forms.ModelForm):
    class Meta:
        model = Glyph
        fields = []

class GrammarNoteForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GrammarNote
        fields = ['body']