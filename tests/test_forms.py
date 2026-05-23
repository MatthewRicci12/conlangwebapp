from django.test import TestCase
from conlangapp.forms import *
import datetime as dt
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
# I am not testing UserForm because that is all Django.

class SubmitTextFormTest(TestCase):
    def setUp(self):
        pass

    def test_missing_title(self):
        form = SubmitTextForm(data={'body': 'Body'})
        self.assertFalse(form.is_valid())

    def test_missing_body(self):
        form = SubmitTextForm(data={'title': 'Title'})
        self.assertFalse(form.is_valid())

    def test_date_added_is_excluded(self):
        form = SubmitTextForm(data={'title': 'Title', 'body': 'Body', 'date_added': dt.date.today()})
        self.assertNotIn('date_added', form.fields)

class UploadFileFormTest(TestCase):
    def setUp(self):
        pass

    def test_valid_file(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")

        uploaded_file = SimpleUploadedFile("test.txt", b"Test Content", content_type="text/plain")

        form = UploadFileForm(
            data={},
            files={"file": uploaded_file}
        )
        self.assertTrue(form.is_valid())

        self.client.force_login(user)
        response = self.client.post(reverse('handle-file'), data={"file": uploaded_file})

        self.assertEqual(response.status_code, 200)

        text = Text.objects.filter(title="test")[0]
        self.assertEqual(text.title, "test")
        self.assertEqual(text.body, "Test Content")

    #form = UploadFileForm(request.POST, request.FILES)
    def test_missing_file(self):
        form = UploadFileForm()
        self.assertFalse(form.is_valid())


class VocabularyEntryFormTest(TestCase):
    def setUp(self):
        pass

    def test_invalid_part_of_speech(self):
        form = VocabularyEntryForm(data={'part_of_speech': 14})
        self.assertFalse(form.is_valid())

    def test_all_valid_parts_of_speech(self):
        form = VocabularyEntryForm(data={'definition': 'Definition'})
        for i in range(int(max(VocabularyEntry.PartOfSpeech)) + 1):
            form.data['part_of_speech'] = VocabularyEntry.PartOfSpeech(i)
            self.assertTrue(form.is_valid())

class GlyphFormTest(TestCase):
    def setUp(self):
        pass

    def test_missing_glyph_string(self):
        form = GlyphForm()
        self.assertFalse(form.is_valid())

class GrammarNoteFormTest(TestCase):
    def setUp(self):
        pass

    def test_missing_body(self):
        form = GrammarNoteForm()
        self.assertFalse(form.is_valid())