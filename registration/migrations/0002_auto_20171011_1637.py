# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 20:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='address1',
            field=models.CharField(default='000 Mockingbird Way', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2017, 10, 11, 20, 37, 22, 837017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='city',
            field=models.CharField(default='Tysons Corner', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='country',
            field=models.CharField(default='USA', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='email',
            field=models.CharField(default='a@a.a', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='phone',
            field=models.CharField(default='000-000-0000', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='postalCode',
            field=models.CharField(default='00000', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='state',
            field=models.CharField(default='VA', max_length=200),
        ),
    ]
