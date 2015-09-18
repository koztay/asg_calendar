# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0013_auto_20150916_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nazwa', max_length=255)),
                ('logo', models.ImageField(upload_to='logos', null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True, verbose_name='strona www')),
                ('description', models.TextField(null=True, blank=True, verbose_name='opis')),
            ],
            options={
                'verbose_name': 'grupa',
                'verbose_name_plural': 'grupy',
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'wydarzenie', 'verbose_name_plural': 'wydarzenia'},
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 17, 23, 12, 27, 903685)),
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='posters', null=True, blank=True, verbose_name='zdjecie'),
        ),
    ]
