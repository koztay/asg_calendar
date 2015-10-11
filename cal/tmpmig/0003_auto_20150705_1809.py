# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20150705_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='event',
            field=models.ForeignKey(default=1, verbose_name='wydarzenie', to='cal.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 7, 5, 18, 8, 46, 612314)),
        ),
    ]
