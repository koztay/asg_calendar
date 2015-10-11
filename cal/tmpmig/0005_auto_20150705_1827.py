# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_auto_20150705_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slot',
            field=models.OneToOneField(blank=True, null=True, to='cal.Slot'),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 7, 5, 18, 27, 27, 326059)),
        ),
    ]
