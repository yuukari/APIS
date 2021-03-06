# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0059_merge_20171114_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='address1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='postalCode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]
