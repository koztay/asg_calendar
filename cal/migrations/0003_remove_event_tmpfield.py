# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20151011_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tmpfield',
        ),
    ]
