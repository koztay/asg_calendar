# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150917_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Numer telefonu musi zostać wpisany w formacie: '+999999999'.")]),
        ),
    ]
