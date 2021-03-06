from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='sample@mail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, 'test123456')


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
        """Test that we can create an new admin user with right attributes"""
        user = get_user_model().objects.create_superuser(
            'admin@email.com',
            'admin123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
