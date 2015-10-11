# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0015_auto_20150917_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 19, 42, 29, 71255), verbose_name='data i czas'),
        ),
        migrations.AddField(
            model_name='faction',
            name='event',
            field=models.ForeignKey(to='cal.Event'),
        ),
        migrations.AddField(
            model_name='entry',
            name='faction',
            field=models.ForeignKey(blank=True, to='cal.Faction', null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='faction',
            field=models.ForeignKey(default=1, to='cal.Faction'),
            preserve_default=False,
        ),
    ]
