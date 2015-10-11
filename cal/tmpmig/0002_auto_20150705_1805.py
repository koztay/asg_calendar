# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user', models.ForeignKey(verbose_name='użytkownik', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'zapis',
                'verbose_name_plural': 'zapisy',
                'ordering': ['pk'],
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 7, 5, 18, 5, 22, 964144)),
        ),
    ]
