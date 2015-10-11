# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0039_auto_20151011_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tmpfield',
            field=models.TextField(blank=True, null=True),
        ),
    ]
