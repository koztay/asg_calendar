# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0005_auto_20150705_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='pic',
            new_name='poster',
        ),
        migrations.AddField(
            model_name='event',
            name='ammo',
            field=models.TextField(blank=True, verbose_name='amunicja', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='areamap',
            field=models.FileField(blank=True, verbose_name='mapa', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='opis', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='entry_fee',
            field=models.TextField(blank=True, verbose_name='wpisowe', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='fps',
            field=models.TextField(blank=True, verbose_name='fps', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='info',
            field=models.TextField(blank=True, verbose_name='wiecej informacji', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location_video',
            field=models.URLField(blank=True, verbose_name='miejsce zbiorki (video)', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pyro',
            field=models.BooleanField(default=False, verbose_name='pirotechnika'),
        ),
        migrations.AddField(
            model_name='event',
            name='rules',
            field=models.TextField(blank=True, verbose_name='zasady gry', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='slot_limit',
            field=models.PositiveIntegerField(blank=True, default=None, verbose_name='limit miejsc', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='terms',
            field=models.TextField(blank=True, verbose_name='regulamin', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='underage',
            field=models.BooleanField(default=False, verbose_name='nieletni'),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 0, 52, 21, 160223), verbose_name='data i czas'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
