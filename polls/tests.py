from django.contrib.auth.models import User
from django.test import TestCase
import datetime
# Create your tests here.


class CreateUserTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_creation(self):
        u = User(email="gophan1992@gmail.com", password='111')
        u.created_at = datetime.datetime.now()
        u.save()
        self.assertEqual(u.email, 'gophan1992@gmail.com')