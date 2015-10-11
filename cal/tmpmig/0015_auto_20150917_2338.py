# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0014_auto_20150917_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 17, 23, 38, 37, 874528)),
        ),
    ]
