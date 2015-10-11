# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_squashed_0045_remove_event_tmpfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tmpfield',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='event',
            field=models.ForeignKey(to='cal.Event', verbose_name='wydarzenie'),
        ),
    ]
