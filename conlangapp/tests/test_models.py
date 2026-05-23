from django.test import TestCase
from django.db import IntegrityError
from ..models import *

# Often you will add a test class for each model/view/form you want to test, with individual methods for testing specific functionality.
# In other cases you may wish to have a separate class for testing a specific use case, with individual test functions that test aspects
# of that use-case (for example, a class to test that a model field is properly validated, with functions to test each of the possible failure
# cases). Again, the structure is very much up to you, but it is best if you are consistent.

class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        self.user = User.objects.create_user(
            username="Matthew123",
            email="MatthewRicci@mattmail.com",
            password="VeryStrongPassword456",
        )

    def test_user_created(self):
        self.assertEqual(User.objects.count(), 1)

    # Uniqueness violations are expressed via db.IntegrityError
    # https://docs.djangoproject.com/en/5.0/_modules/django/db/utils/
    def test_email_is_unique(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="otheruser",
                email="test@example.com",
                password="password",
            )

    def test_user_has_pk(self):
        self.assertIsNotNone(self.user.user_id)

    def test_password_is_hashed(self):
        self.assertNotEqual(self.user.password, "VeryStrongPassword456")
        self.assertTrue(self.user.check_password("VeryStrongPassword456"))


class TokenTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Matthew123", email="MatthewRicci@mattmail.com", password="VeryStrongPassword456")
        self.token = Token.objects.create(surface_form="hello", user=self.user)

    def test_token_created(self):
        self.assertEqual(Token.objects.count(), 1)

    def test_token_has_pk(self):
        self.assertIsNotNone(self.token.token_id)

    def test_token_surface_form(self):
        self.assertEqual(self.token.surface_form, "hello")

    def test_token_fk_to_user(self):
        self.assertEqual(self.token.user, self.user)

    def test_token_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(Token.objects.count(), 0)

    def test_token_accessible_from_user(self):
        self.assertIn(self.token, self.user.tokens.all())


class GrammarNoteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", email="u@x.com", password="pw")
        self.note = GrammarNote.objects.create(
            title="My Note", body="Some grammar content.", user=self.user
        )

    def test_grammar_note_created(self):
        self.assertEqual(GrammarNote.objects.count(), 1)

    def test_grammar_note_has_pk(self):
        self.assertIsNotNone(self.note.gn_id)

    def test_default_title(self):
        note = GrammarNote.objects.create(user=self.user)
        self.assertEqual(note.title, "Grammar Note")

    def test_body_can_be_blank(self):
        note = GrammarNote.objects.create(user=self.user, body="")
        self.assertEqual(note.body, "")

    def test_grammar_note_fk_to_user(self):
        self.assertEqual(self.note.user, self.user)

    def test_grammar_note_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(GrammarNote.objects.count(), 0)

    def test_grammar_note_accessible_from_user(self):
        self.assertIn(self.note, self.user.grammar_notes.all())
