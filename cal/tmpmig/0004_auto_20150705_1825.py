# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20150705_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nazwa')),
            ],
            options={
                'verbose_name_plural': 'sloty',
                'verbose_name': 'slot',
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 7, 5, 18, 25, 14, 917174)),
        ),
        migrations.AddField(
            model_name='slot',
            name='event',
            field=models.ForeignKey(to='cal.Event'),
        ),
    ]
