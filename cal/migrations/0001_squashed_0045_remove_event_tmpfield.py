# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import location_field.models.plain
import datetime
from django.conf import settings


class Migration(migrations.Migration):


    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='tytuł', max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 16, 2, 11, 57, 674247))),
                ('location', location_field.models.plain.PlainLocationField(default='53.43,14.56', max_length=63)),
                ('poster', models.ImageField(verbose_name='zdjecie', upload_to='terrains', null=True, blank=True)),
                ('created_by', models.ForeignKey(verbose_name='stworzone przez', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('ammo', models.TextField(verbose_name='amunicja', null=True, blank=True)),
                ('areamap', models.FileField(verbose_name='mapa', upload_to='', null=True, blank=True)),
                ('description', models.TextField(verbose_name='opis', null=True, blank=True)),
                ('entry_fee', models.TextField(verbose_name='wpisowe', null=True, blank=True)),
                ('fps', models.TextField(verbose_name='fps', null=True, blank=True)),
                ('info', models.TextField(verbose_name='wiecej informacji', null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('location_video', models.URLField(verbose_name='miejsce zbiorki (video)', null=True, blank=True)),
                ('pyro', models.BooleanField(verbose_name='pirotechnika', default=False)),
                ('rules', models.TextField(verbose_name='zasady gry', null=True, blank=True)),
                ('slot_limit', models.PositiveIntegerField(verbose_name='limit miejsc', null=True, default=None, blank=True)),
                ('terms', models.TextField(verbose_name='regulamin', null=True, blank=True)),
                ('underage', models.BooleanField(verbose_name='nieletni', default=False)),
            ],
            options={
                'verbose_name': 'wydarzenie',
                'verbose_name_plural': 'wydarzenia',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.ForeignKey(verbose_name='użytkownik', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(verbose_name='wydarzenie', default=1, to='cal.Event')),
            ],
            options={
                'verbose_name': 'zapis',
                'verbose_name_plural': 'zapisy',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='nazwa', max_length=200)),
                ('event', models.ForeignKey(to='cal.Event')),
            ],
            options={
                'verbose_name': 'slot',
                'verbose_name_plural': 'sloty',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='slot',
            field=models.OneToOneField(null=True, to='cal.Slot', blank=True),
        ),
        migrations.CreateModel(
            name='PGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='nazwa', max_length=255)),
                ('logo', models.ImageField(upload_to='logos', null=True, blank=True)),
                ('website', models.URLField(verbose_name='strona www', null=True, blank=True)),
                ('description', models.TextField(verbose_name='opis', null=True, blank=True)),
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
            field=models.ImageField(verbose_name='zdjecie', upload_to='posters', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 17, 23, 38, 37, 874528)),
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 18, 19, 42, 29, 71255)),
        ),
        migrations.AddField(
            model_name='faction',
            name='event',
            field=models.ForeignKey(to='cal.Event'),
        ),
        migrations.AddField(
            model_name='entry',
            name='faction',
            field=models.ForeignKey(null=True, blank=True, to='cal.Faction'),
        ),
        migrations.AddField(
            model_name='slot',
            name='faction',
            field=models.ForeignKey(default=1, to='cal.Faction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 18, 19, 48, 23, 881309)),
        ),
        migrations.AlterModelOptions(
            name='faction',
            options={'verbose_name': 'frakcja', 'verbose_name_plural': 'frakcje'},
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 18, 20, 12, 26, 391857)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 35, 59, 284050)),
        ),
        migrations.RemoveField(
            model_name='slot',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 47, 27, 908846)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 50, 38, 844502)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 51, 59, 252964)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 52, 4, 665388)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 9, 19, 12, 52, 35, 79054)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 8, 14, 21, 34, 401280)),
        ),
        migrations.AddField(
            model_name='event',
            name='endtime1',
            field=models.TimeField(verbose_name='koniec1', default=datetime.datetime(2015, 10, 9, 16, 3, 54, 463427)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='endtime2',
            field=models.TimeField(verbose_name='koniec2', default=datetime.datetime(2015, 10, 9, 16, 4, 6, 668311)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='starttime1',
            field=models.TimeField(verbose_name='rozgrywki1', default=datetime.datetime(2015, 10, 9, 16, 4, 14, 471744)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='starttime2',
            field=models.TimeField(verbose_name='rozgrywki2', default=datetime.datetime(2015, 10, 9, 16, 4, 19, 976166)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 9, 16, 3, 26, 552905)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 10, 17, 23, 16, 378281)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 10, 19, 16, 44, 563232)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 50, 52, 951954)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 51, 1, 158214)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 51, 9, 856840)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 51, 57, 641118)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 51, 59, 987996)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 11, 52, 3, 18193)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 9, 57, 21, 923396, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 9, 57, 35, 314821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 9, 57, 40, 956021, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=datetime.datetime(2015, 10, 11, 9, 57, 50, 621029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(verbose_name='data i czas', default=django.utils.timezone.now),
        ),
    ]
