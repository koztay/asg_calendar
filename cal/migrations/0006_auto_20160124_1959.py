# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0005_auto_20160124_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='event',
        ),
        migrations.AlterField(
            model_name='entry',
            name='slot',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cal.Slot'),
        ),
    ]
