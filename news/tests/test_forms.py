from django.test import TestCase

from news.forms import RedactorForm


class FormTest(TestCase):
    def test_redactor_creation_form(self):
        form_data = {
            "username": "test_username",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "test_name",
            "last_name": "test_surname",
            "workplace": None,
            "email": "test@test.com",
            "years_of_experience": 10
        }

        form = RedactorForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
