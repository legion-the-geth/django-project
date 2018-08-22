# Generated by Django 2.0.5 on 2018-08-22 14:31

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='created at')),
                ('category', models.CharField(choices=[(accounts.models.GroupCat('Pollers'), 'Pollers'), (accounts.models.GroupCat('Moderators'), 'Moderators'), (accounts.models.GroupCat('Administrators'), 'Administrators')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=15, validators=[accounts.models.validate_pw])),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(auto_now=True, verbose_name='registrered')),
                ('groups', models.ManyToManyField(to='accounts.Group')),
            ],
        ),
    ]
