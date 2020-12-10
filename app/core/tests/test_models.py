from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creatin a new user with an email is successful"""
        email = 'test@mail.com'
        password = 'test123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123456')

    def test_create_new_super_user(self):
        """"""
        user = get_user_model().objects.create_superuser(
            'admin@email.com',
            'admin123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
