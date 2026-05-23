from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client
from conlangapp.models import *
import tempfile
import json

class IndexViewTest(TestCase):
    def setUp(self):
        pass

    def test_get_renders_correctly(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

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

class SubmitTokenViewTest(TestCase):
    def setUp(self):
        pass

    def test_renders_current_form_partial(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk

        response = self.client.get(reverse('submit-token', args=[text_pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/current_form.html')

class UserClicksTextViewTest(TestCase):
    def setUp(self):
        pass

    def test_get_renders_correctly(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk
        response = self.client.get(reverse('submit-token', args=[text_pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/current_form.html')


    def test_post_with_form_up(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk
        data={'form_up': 1}

        response = self.client.post(reverse('user-clicks-text', args=[text_pk]), data=data)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['form_up'])


    def test_post_with_token(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk
        data={'token': 'fawefawefawef'}

        response = self.client.post(reverse('user-clicks-text', args=[text_pk]), data=data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['form_div_context']['token'], 'fawefawefawef')

    def test_post_submits_forms(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        text = Text.objects.create(
            title="Title", body="Body", user=user
        )
        text_pk = text.pk
        data={'selected_form': 'vocabulary_entry_form'}

        response = self.client.post(reverse('user-clicks-text', args=[text_pk]), data=data)

        self.assertEqual(response.context['form_div_context']['selected_form'], 'vocabulary_entry_form')

        data={'selected_form': 'glyph_form'}

        response = self.client.post(reverse('user-clicks-text', args=[text_pk]), data=data)

        self.assertEqual(response.context['form_div_context']['selected_form'], 'glyph_form')

        data={'selected_form': 'grammar_note_form'}

        response = self.client.post(reverse('user-clicks-text', args=[text_pk]), data=data)

        self.assertEqual(response.context['form_div_context']['selected_form'], 'grammar_note_form')

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

    def test_get_renders_all_glyphs(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")

        glyph_strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        for glyph_string in glyph_strings:
            Glyph(user=user, glyph_string=glyph_string).save()

        response = self.client.get(reverse('phonology-and-glyphs-tab'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Glyph.objects.all()), 7)


    def test_post_with_glyph_id_sets_selected_glyph(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        glyph = Glyph.objects.create(glyph_string='a', user=user)
        glyph_pk = glyph.pk
        data = {'glyph_id': glyph_pk}

        response = self.client.post(reverse('phonology-and-glyphs-tab'), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['currently_selected_glyph_id'], 1)

    def test_post_with_null_glyph_id(self):
        glyph_pk = 'null'
        data = {'glyph_id': glyph_pk}

        response = self.client.post(reverse('phonology-and-glyphs-tab'), data=data)

        self.assertEqual(response.status_code, 200)

        self.assertIsNone(response.context['currently_selected_glyph_id'])

    def test_post_with_selected_ipa_symbol_creates_mapping(self):
        user = User.objects.create_user(username="MatthewRicci123", email="email@email.com", password="password")
        glyph = Glyph.objects.create(glyph_string='a', user=user)
        glyph_pk = glyph.pk
        data = {'selected_ipa_symbol': 'o', 'selected_glyph_pk': glyph_pk}

        self.client.force_login(user)
        response = self.client.post(reverse('phonology-and-glyphs-tab'), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Glyph.objects.get(pk=glyph_pk).phonology_mappings.all()[0].ipa_symbol == 'o')

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

    def helper_test_chooses_right_model(self, model):
        data = {'model': model, 'primary_key': 1}

        response = self.client.get(reverse('modal'), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['which_model'], model)
        self.assertEqual(int(response.context['pk']), 1)

    def test_chooses_right_model(self):
        self.helper_test_chooses_right_model('Glyph')
        self.helper_test_chooses_right_model('Text')
        self.helper_test_chooses_right_model('VocabularyEntry')
        self.helper_test_chooses_right_model('GrammarNote')

    def test_post_not_allowed(self):
        response = self.client.post(reverse('modal'))
        self.assertContains(response, '', status_code=405)

# Dunno if I'm goin to do a basic Auth system or not yet.
# class LogInViewTest(TestCase):
#     def setUp(self):
#         pass
#
# class SignUpViewTest(TestCase):
#     def setUp(self):
#         pass


