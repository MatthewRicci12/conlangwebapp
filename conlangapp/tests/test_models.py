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



class VocabularyEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", email="u@x.com", password="pw")
        self.entry = VocabularyEntry.objects.create(
            definition="a feline animal",
            part_of_speech=VocabularyEntry.PartOfSpeech.NOUN,
            user=self.user,
        )

    def test_vocabulary_entry_created(self):
        self.assertEqual(VocabularyEntry.objects.count(), 1)

    def test_vocabulary_entry_has_pk(self):
        self.assertIsNotNone(self.entry.ve_id)

    def test_default_part_of_speech(self):
        entry = VocabularyEntry.objects.create(definition="thing", user=self.user)
        self.assertEqual(entry.part_of_speech, VocabularyEntry.PartOfSpeech.UNDECIDED)

    def test_part_of_speech_choices(self):
        for member in VocabularyEntry.PartOfSpeech:
            entry = VocabularyEntry.objects.create(
                definition="word", part_of_speech=member, user=self.user
            )
            self.assertEqual(entry.part_of_speech, member)

    def test_grammar_tag_nullable(self):
        entry = VocabularyEntry.objects.create(definition="word", user=self.user)
        self.assertIsNone(entry.grammar_tag)

    def test_vocabulary_entry_fk_to_user(self):
        self.assertEqual(self.entry.user, self.user)

    def test_vocabulary_entry_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(VocabularyEntry.objects.count(), 0)

    def test_vocabulary_entry_accessible_from_user(self):
        self.assertIn(self.entry, self.user.vocabulary_entries.all())


class TextModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", email="u@x.com", password="pw")
        self.text = Text.objects.create(
            title="Story", body="Once upon a time...", user=self.user
        )

    def test_text_created(self):
        self.assertEqual(Text.objects.count(), 1)

    def test_text_has_pk(self):
        self.assertIsNotNone(self.text.text_id)

    def test_default_title(self):
        text = Text.objects.create(body="...", user=self.user)
        self.assertEqual(text.title, "Title")

    def test_date_added_auto_set(self):
        self.assertIsNotNone(self.text.date_added)

    def test_text_fk_to_user(self):
        self.assertEqual(self.text.user, self.user)

    def test_text_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(Text.objects.count(), 0)

    def test_text_accessible_from_user(self):
        self.assertIn(self.text, self.user.texts.all())


class PhonologyMappingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", email="u@x.com", password="pw")
        self.pm = PhonologyMapping.objects.create(
            ipa_symbol="p",
            phonological_status=PhonologyMapping.PhonologicalStatus.PHONEME,
            distribution="word-initial",
            user=self.user,
        )

    def test_phonology_mapping_created(self):
        self.assertEqual(PhonologyMapping.objects.count(), 1)

    def test_phonology_mapping_has_pk(self):
        self.assertIsNotNone(self.pm.pm_id)

    def test_default_phonological_status(self):
        pm = PhonologyMapping.objects.create(user=self.user)
        self.assertEqual(pm.phonological_status, PhonologyMapping.PhonologicalStatus.UNDECIDED)

    def test_ipa_symbol_nullable(self):
        pm = PhonologyMapping.objects.create(user=self.user)
        self.assertIsNone(pm.ipa_symbol)

    def test_phonology_mapping_fk_to_user(self):
        self.assertEqual(self.pm.user, self.user)

    def test_phonology_mapping_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(PhonologyMapping.objects.count(), 0)

    def test_phonology_mapping_accessible_from_user(self):
        self.assertIn(self.pm, self.user.phonology_mappings.all())


class GlyphModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", email="u@x.com", password="pw")
        self.pm1 = PhonologyMapping.objects.create(ipa_symbol="p", user=self.user)
        self.pm2 = PhonologyMapping.objects.create(ipa_symbol="b", user=self.user)
        self.glyph = Glyph.objects.create(glyph_string="π", user=self.user)
        self.glyph.phonology_mappings.set([self.pm1, self.pm2])

    def test_glyph_created(self):
        self.assertEqual(Glyph.objects.count(), 1)

    def test_glyph_has_pk(self):
        self.assertIsNotNone(self.glyph.glyph_id)

    def test_glyph_string(self):
        self.assertEqual(self.glyph.glyph_string, "π")

    def test_glyph_fk_to_user(self):
        self.assertEqual(self.glyph.user, self.user)

    def test_glyph_m2m_phonology_mappings(self):
        self.assertIn(self.pm1, self.glyph.phonology_mappings.all())
        self.assertIn(self.pm2, self.glyph.phonology_mappings.all())

    def test_glyph_reverse_m2m(self):
        self.assertIn(self.glyph, self.pm1.glyphs.all())

    def test_glyph_deleted_with_user(self):
        self.user.delete()
        self.assertEqual(Glyph.objects.count(), 0)

    def test_m2m_survives_one_pm_deletion(self):
        # Deleting one PM should only remove it from the M2M, not the glyph
        self.pm1.delete()
        self.glyph.refresh_from_db()
        self.assertEqual(self.glyph.phonology_mappings.count(), 1)
        self.assertIn(self.pm2, self.glyph.phonology_mappings.all())

    def test_glyph_accessible_from_user(self):
        self.assertIn(self.glyph, self.user.glyphs.all())