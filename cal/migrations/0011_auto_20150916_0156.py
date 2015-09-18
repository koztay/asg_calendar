# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0010_auto_20150916_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 1, 56, 6, 468783), verbose_name='data i czas'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='Point(54.0 15.0)', max_length=63),
        ),
        migrations.AlterField(
            model_name='event',
            name='location_helper',
            field=models.CharField(default='Szczecin', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(verbose_name='tytuł', max_length=255),
        ),
    ]
