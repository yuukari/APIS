# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='volunteerDepts',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
