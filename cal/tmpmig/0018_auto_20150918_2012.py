# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0017_auto_20150918_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faction',
            options={'verbose_name_plural': 'frakcje', 'verbose_name': 'frakcja'},
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 18, 20, 12, 26, 391857)),
        ),
    ]
