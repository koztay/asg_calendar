# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0009_auto_20160313_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='user',
            field=models.ManyToManyField(related_name='factions', through='cal.Entry', to=settings.AUTH_USER_MODEL, verbose_name='użytkownicy'),
        ),
    ]