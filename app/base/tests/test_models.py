from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):
    def test_user_login_details(self):
        email = 'kells@kells.com'
        password = 'P@ssword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalize(self):
        email = 'kells@KELLS:COM'
        user = get_user_model().objects.create_user(
            email, 'test123'
        )
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_email_not_valid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test123'
            )

    def test_if_superuser(self):
        email = 'kells@KELLS:COM'
        user = get_user_model().objects.create_superuser(
            email=email, 
            password='test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)