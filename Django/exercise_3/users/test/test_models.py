from django.test import TestCase
from ..models import Profile
from django.contrib.auth.models import User


class ProfileTests(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='testuser', password='secret_password')

    def test_should_return_true_when_profile_is_created(self):
        self.assertEqual(str(self.user_1.profile), 'Profile of testuser')
