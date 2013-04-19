from django.db import IntegrityError
from models import User


class TaskManager(object):
    
    def create_user(self, username, email, snooze_seconds=10*60):
        try:
            user = User.objects.create(username=username, email=email, snooze_seconds=snooze_seconds)
            return user.id
        except IntegrityError:
            raise Exception("That username already exists. Please try another.")

    def add_task(self, username, title, description=None, expire_date=None, reminders=None):
        """
        Create a task
        """
        pass


