from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ChoiceField
from .models import *

# Always get whatever AUTH_USER_MODEL points to instead of importing User directly

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] #TODO: Add email


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
    glyph_string = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Glyph
        fields = ['glyph_string']

class GrammarNoteForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = GrammarNote
        fields = ['body']