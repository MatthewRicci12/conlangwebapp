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
        pass


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

class PhonologyAndGlyphsTabViewTest(TestCase):
    def setUp(self):
        pass

class GrammarTabViewTest(TestCase):
    def setUp(self):
        pass


class ModalViewTest(TestCase):
    def setUp(self):
        pass

class LogInViewTest(TestCase):
    def setUp(self):
        pass

class SignUpViewTest(TestCase):
    def setUp(self):
        pass


