# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0011_auto_20150916_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 16, 2, 8, 40, 841882)),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, default='53.5,14.7'),
        ),
    ]
