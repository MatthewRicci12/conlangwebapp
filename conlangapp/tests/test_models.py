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
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username="Matthew123", email="MatthewRicci@mattmail.com", password="VeryStrongPassword456")
        self.token = Token.objects.create(surface_form="hello", user=self.user)

        