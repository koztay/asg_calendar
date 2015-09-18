# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0009_auto_20150916_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_helper',
            field=models.CharField(max_length=200, default='Szczecin'),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 16, 1, 44, 42, 87885)),
        ),
    ]
