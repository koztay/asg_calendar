# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0012_auto_20150916_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location_helper',
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 2, 11, 57, 674247), verbose_name='data i czas'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='53.43,14.56', max_length=63),
        ),
    ]
