# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_eventpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factions', to='cms.EventPage')),
            ],
            options={
                'verbose_name_plural': 'frakcje',
                'verbose_name': 'frakcja',
            },
        ),
    ]
