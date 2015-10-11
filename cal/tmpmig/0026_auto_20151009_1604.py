# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0025_auto_20151008_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endtime1',
            field=models.TimeField(default=datetime.datetime(2015, 10, 9, 16, 3, 54, 463427), verbose_name='koniec1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='endtime2',
            field=models.TimeField(default=datetime.datetime(2015, 10, 9, 16, 4, 6, 668311), verbose_name='koniec2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='starttime1',
            field=models.TimeField(default=datetime.datetime(2015, 10, 9, 16, 4, 14, 471744), verbose_name='rozgrywki1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='starttime2',
            field=models.TimeField(default=datetime.datetime(2015, 10, 9, 16, 4, 19, 976166), verbose_name='rozgrywki2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 16, 3, 26, 552905), verbose_name='data i czas'),
        ),
    ]
