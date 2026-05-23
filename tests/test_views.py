from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from conlangapp.models import *
import json

class IndexViewTest(TestCase):
    def setUp(self):
        pass

    def test_get_renders_correctly(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'conlangapp/templates/index.html')

    def test_post_with_primary_key_triggers_update(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk
        post_params = json.dumps({'title': 'New Title', 'body': 'New Body'})

        response = self.client.post(reverse('index'), data={'primary_key': text_pk, 'params': post_params})

        updated_text = Text.objects.get(pk=text_pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_text.title, 'New Title')
        self.assertEqual(updated_text.body, 'New Body')

    def test_get_with_primary_key_triggers_delete(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk

        response = self.client.get(reverse('index'), data={'primary_key': text_pk})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Text.objects.filter(pk=text_pk).exists())

class HandleFileViewTest(TestCase):
    def setUp(self):
        pass

class SubmitTokenViewTest(TestCase):
    def setUp(self):
        pass

class EnterTextScreenViewTest(TestCase):
    def setUp(self):
        pass

class UserClicksTextViewTest(TestCase):
    def setUp(self):
        pass

class VocabularyListViewTest(TestCase):
    def setUp(self):
        pass

    def test_post_with_primary_key_triggers_update(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        ve = VocabularyEntry.objects.create(tokens="hello", definition="A greeting", part_of_speech=VocabularyEntry.PartOfSpeech.NOUN,
        user=user, grammar_tag="Greetings in general")
        ve_pk = ve.pk
        post_params = json.dumps({'definition': "Another definition", 'part_of_speech': VocabularyEntry.PartOfSpeech.VERB})

        response = self.client.post(reverse('vocabulary-list'), data={'primary_key': ve_pk, 'params': post_params})

        updated_ve = VocabularyEntry.objects.get(pk=ve_pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_ve.definition, "Another definition")
        self.assertEqual(updated_ve.part_of_speech, VocabularyEntry.PartOfSpeech.VERB)


    def test_get_with_primary_key_triggers_delete(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        ve = VocabularyEntry.objects.create(tokens="hello", definition="A greeting", part_of_speech=VocabularyEntry.PartOfSpeech.NOUN,
        user=user, grammar_tag="Greetings in general")
        ve_pk = ve.pk

        response = self.client.get(reverse('vocabulary-list'), data={'primary_key': ve_pk})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(VocabularyEntry.objects.filter(pk=ve_pk).exists())

class PhonologyAndGlyphsTabViewTest(TestCase):
    def setUp(self):
        pass

    def test_post_with_primary_key_triggers_update(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        glyph = Glyph.objects.create(glyph_string='a', user=user)
        glyph_pk = glyph.pk
        post_params = json.dumps({'glyph_string': 'b'})

        response = self.client.post(reverse('phonology-and-glyphs-tab'), data={'primary_key': glyph_pk, 'params': post_params})

        updated_glyph = Glyph.objects.get(pk=glyph_pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_glyph.glyph_string, 'b')

    def test_get_with_primary_key_triggers_delete(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        glyph = Glyph.objects.create(glyph_string='a', user=user)
        glyph_pk = glyph.pk

        response = self.client.get(reverse('phonology-and-glyphs-tab'), data={'primary_key': glyph_pk})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Glyph.objects.filter(pk=glyph_pk).exists())

class GrammarTabViewTest(TestCase):
    def setUp(self):
        pass

    def test_post_with_primary_key_triggers_update(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        gn = GrammarNote.objects.create(title="verb conjugation", body="conjugation tables", user=user)
        gn_pk = gn.pk
        post_params = json.dumps({'body': 'New Body'})

        response = self.client.post(reverse('grammar-tab'), data={'primary_key': gn_pk, 'params': post_params})

        updated_gn = GrammarNote.objects.get(pk=gn_pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_gn.body, 'New Body')

    def test_get_with_primary_key_triggers_delete(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        gn = GrammarNote.objects.create(title="verb conjugation", body="conjugation tables", user=user)
        gn_pk = gn.pk

        response = self.client.get(reverse('grammar-tab'), data={'primary_key': gn_pk})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(GrammarNote.objects.filter(pk=gn_pk).exists())

class ModalViewTest(TestCase):
    def setUp(self):
        pass

class LogInViewTest(TestCase):
    def setUp(self):
        pass

class SignUpViewTest(TestCase):
    def setUp(self):
        pass


