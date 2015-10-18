# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20151011_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='created_by',
            new_name='owner',
        ),
    ]
