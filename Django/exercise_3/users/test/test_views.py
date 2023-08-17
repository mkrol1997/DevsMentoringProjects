from django.test.client import Client
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from datetime import date
from django.contrib.auth import get_user_model
from django.core import mail


class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_superuser(
            username='testuser',
            password='secret',
        )

    def test_should_return_true_if_user_login_valid_credentials(self):
        credentials = {
                'username': 'testuser',
                'password': 'secret'
            }
        login_status = self.client.login(**credentials)
        self.assertEqual(login_status, True)

    def test_should_return_false_if_user_login_invalid_credentials(self):
        credentials = {
                'username': 'testuser',
                'password': 'wrong-password'
            }
        login_status = self.client.login(**credentials)
        self.assertEqual(login_status, False)

    def test_should_return_true_if_get_request_profile_view_after_login(self):
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/profile.html')

    def test_should_return_true_if_recent_invalid_login_date_updated_with_signal(self):
        wrong_credentials = {
            'username': 'testuser',
            'password': 'wrong-password'
            }

        with patch('users.signals.datetime') as mock_date:
            date_today_mock = date(year=2010, month=10, day=8)
            mock_date.today.return_value = date_today_mock

            self.client.login(**wrong_credentials)

        # self.test_user.profile.last_failed_login
        test_user = get_user_model().objects.get(username=wrong_credentials['username'])
        recent_invalid_login = test_user.profile.last_failed_login

        self.assertEqual(recent_invalid_login, date(2010, 10, 8))


class TestProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_should_return_true_when_user_logged_with_response_status_code_200(self):
        self.client.force_login(self.test_user)

        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_should_return_true_when_not_logged_user_visits_profile(self):
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 302)


class TestsUserRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_return_true_when_view_requested_with_get_method(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_should_return_true_when_user_registered_correctly(self):
        registration_form_data = {
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'Secret12344321!',
            'password2': 'Secret12344321!'
        }

        response = self.client.post(reverse('register'), data=registration_form_data)
        users = get_user_model().objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(users.count(), 1)


class TestsUserPasswordReset(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

    def test_can_reset_password(self) -> None:
        response = self.client.get(reverse('password_reset'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pw_reset/pw_reset.html')

        response = self.client.post(reverse('password_reset'), {'email': 'test@email.com'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset on testserver')

        token = response.context[0]['token']
        uid = response.context[0]['uid']
        response = self.client.get(reverse('password_reset_done'), kwargs={'token': token, 'uidb64': uid})

        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('password_reset_confirm',
                                            kwargs={'token': token, 'uidb64': uid}),
                                    data={'new_password1': 'pass', 'new_password2': 'pass'})
        self.assertEqual(response.status_code, 302)

        credendialts = {
            'username': 'testuser',
            'password': 'secret',
        }
        self.assertTrue(self.client.login(**credendialts))
