import datetime
from enum import Enum
from django.db import models
from django.utils import timezone

class GroupCat(Enum):
    POLER = 'Pollers'
    MODER = 'Moderators'
    ADMIN = 'Administrators'

    def __str__(self):
        return self.name

    def label(self):
        return self.value

class Group(models.Model):
    name = models.CharField(max_length=150, uniqe=True)
    date_created = models.DateTimeField('created at', auto_now=True)
    category = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in GroupCat]
    )

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    pseudo = models.CharField(max_length=15, unique=True)
    registration_date = models.DateTimeField('registrered', auto_now=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.pseudo

    def registered_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(weeks=1) <= self.registration_date
