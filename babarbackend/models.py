
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=128)
    email = models.CharField(max_length=128, null=True, blank=True)
    snooze_seconds = models.IntegerField(default=10*60) 


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    parent_task_id = models.IntegerField(null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1028, null=True, blank=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    dismissable = models.BooleanField(default=True)
    active = models.BooleanField(default=True)


class Reminders(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.IntegerField()
    description = models.CharField(max_length=128)
    expire_date = models.DateTimeField(null=True, blank=True)
    send_email = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

