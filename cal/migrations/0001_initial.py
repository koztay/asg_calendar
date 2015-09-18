# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200, verbose_name='tytuł')),
                ('datetime', models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 7, 5, 14, 56, 45, 681126, tzinfo=utc))),
                ('location', models.CharField(max_length=200, verbose_name='lokalizacja')),
                ('pic', models.ImageField(blank=True, upload_to='terrains', verbose_name='zdjecie', null=True)),
                ('created_by', models.ForeignKey(verbose_name='stworzone przez', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'wydarzenia',
                'ordering': ['title'],
                'verbose_name': 'wydarzenie',
            },
        ),
    ]
