from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

# Create your tests here.

class RegistrationTest(TestCase):
    def test_registration_success(self):
        # Set up
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }

        # Make POST request
        response = self.client.post(url, data)

        # Assertions
        self.assertEqual(response.status_code, 302)  # Successful registration should redirect
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())  # User should be created in the database
    def test_registration_failure(self):
        # Set up
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password456',  # Mismatched passwords
        }

        # Make POST request
        response = self.client.post(url, data)

        # Assertions
        self.assertEqual(response.status_code, 200)  # Failed registration should return to the same page
        self.assertFalse(CustomUser.objects.filter(username='testuser').exists())  # User should not be created