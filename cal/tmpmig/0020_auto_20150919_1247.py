# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0019_auto_20150919_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 47, 27, 908846)),
        ),
    ]
