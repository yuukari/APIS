# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0054_auto_20170920_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.DateTimeField()),
                ('timeOut', models.DateTimeField(blank=True, null=True)),
                ('detail', models.TextField(blank=True)),
                ('multiplier', models.IntegerField(choices=[(1, 'No Multiplier'), (1.5, '1.5x Multiplier'), (2, '2x Multiplier')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, max_length=250, null=True)),
                ('who', models.CharField(blank=True, max_length=140, null=True)),
                ('expired', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactHandle', models.CharField(blank=True, max_length=50, null=True)),
                ('checkedIn', models.BooleanField(default=False)),
                ('dateEntered', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Badge')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='jobRequest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='volunteer.JobRequest'),
        ),
        migrations.AddField(
            model_name='job',
            name='staffIn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffIn', to='registration.Staff'),
        ),
        migrations.AddField(
            model_name='job',
            name='staffOut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffOut', to='registration.Staff'),
        ),
        migrations.AddField(
            model_name='job',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.Volunteer'),
        ),
    ]
