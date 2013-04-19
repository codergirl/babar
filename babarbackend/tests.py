import unittest

from babarbackend.models import *
from babarbackend.api import *

class UserTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        self.manager = TaskManager()


    def tearDown(self):
        User.objects.all().delete()

    def testCreateUser(self):
        username = 'sara'
        email = 'sara@sara.com'
        snooze_seconds = 90

        user_id = self.manager.create_user(username=username, email=email, snooze_seconds=snooze_seconds)

        user = User.objects.get(id=user_id)
        self.assertEquals(user.username, username)
        self.assertEquals(user.email, email)
        self.assertEquals(user.snooze_seconds, snooze_seconds)

        # same username raises integrity error
        self.assertRaises(Exception, self.manager.create_user, username=username, email=email, snooze_seconds=snooze_seconds)

