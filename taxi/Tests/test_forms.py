from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormTests(TestCase):
    def test_driver_creation_form_with_parameters(self):
        form_data = {
            "username": "user1",
            "password1": "<Password123>",
            "password2": "<Password123>",
            "license_number": "ABC12345",
            "first_name": "John",
            "last_name": "Doe",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
