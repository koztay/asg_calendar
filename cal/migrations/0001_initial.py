# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'zapis',
                'verbose_name_plural': 'zapisy',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='tytuł', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='opis', null=True)),
                ('poster', models.ImageField(upload_to='posters', blank=True, verbose_name='zdjecie', null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data i czas')),
                ('starttime1', models.TimeField(verbose_name='rozgrywki1')),
                ('starttime2', models.TimeField(verbose_name='rozgrywki2')),
                ('endtime1', models.TimeField(verbose_name='koniec1')),
                ('endtime2', models.TimeField(verbose_name='koniec2')),
                ('location', location_field.models.plain.PlainLocationField(default='53.43,14.56', max_length=63)),
                ('location_video', models.URLField(blank=True, verbose_name='miejsce zbiorki (video)', null=True)),
                ('areamap', models.FileField(upload_to='', blank=True, verbose_name='mapa', null=True)),
                ('fps', models.TextField(blank=True, verbose_name='fps', null=True)),
                ('ammo', models.TextField(blank=True, verbose_name='amunicja', null=True)),
                ('terms', models.TextField(blank=True, verbose_name='regulamin', null=True)),
                ('entry_fee', models.TextField(blank=True, verbose_name='wpisowe', null=True)),
                ('slot_limit', models.PositiveIntegerField(default=None, blank=True, verbose_name='limit miejsc', null=True)),
                ('pyro', models.BooleanField(default=False, verbose_name='pirotechnika')),
                ('underage', models.BooleanField(default=False, verbose_name='nieletni')),
                ('rules', models.TextField(blank=True, verbose_name='zasady gry', null=True)),
                ('info', models.TextField(blank=True, verbose_name='wiecej informacji', null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'wydarzenie',
                'verbose_name_plural': 'wydarzenia',
            },
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event', models.ForeignKey(to='cal.Event')),
            ],
            options={
                'verbose_name': 'frakcja',
                'verbose_name_plural': 'frakcje',
            },
        ),
        migrations.CreateModel(
            name='PGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nazwa', max_length=255)),
                ('logo', models.ImageField(upload_to='logos', blank=True, null=True)),
                ('website', models.URLField(blank=True, verbose_name='strona www', null=True)),
                ('description', models.TextField(blank=True, verbose_name='opis', null=True)),
            ],
            options={
                'verbose_name': 'grupa',
                'verbose_name_plural': 'grupy',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nazwa', max_length=200)),
                ('faction', models.ForeignKey(to='cal.Faction')),
            ],
            options={
                'verbose_name': 'slot',
                'verbose_name_plural': 'sloty',
            },
        ),
    ]
