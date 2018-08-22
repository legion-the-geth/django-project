import datetime
from enum import Enum
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def validate_pw(password):
    if 15 < len(password) < 4:
        raise ValidationError(_('Password must contain between 4 and 15 characters'))

class GroupCat(Enum):
    POLER = 'Pollers'
    MODER = 'Moderators'
    ADMIN = 'Administrators'

    def __str__(self):
        return self.name

    def label(self):
        return self.value

class Group(models.Model):
    name = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField('created at', auto_now=True)
    category = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in GroupCat]
    )

    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15, validators=[validate_pw])
    email = models.EmailField(max_length=250, unique=True)
    active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    registration_date = models.DateTimeField('registrered', auto_now=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.login

    def registered_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(weeks=1) <= self.registration_date

    def clean(self):
        if self.age is not None and self.age < 12:
            raise ValidationError(_('You must be at least 12yo to register on this site.'))
