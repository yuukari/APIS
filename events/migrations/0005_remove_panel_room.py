# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-23 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180123_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='room',
        ),
    ]