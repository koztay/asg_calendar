# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0028_auto_20151010_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 50, 52, 951954)),
        ),
    ]
