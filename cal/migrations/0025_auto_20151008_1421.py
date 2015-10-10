# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0024_auto_20150919_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 14, 21, 34, 401280), verbose_name='data i czas'),
        ),
    ]
