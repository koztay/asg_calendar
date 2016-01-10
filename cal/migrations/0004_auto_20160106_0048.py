# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 23:48
from __future__ import unicode_literals

import datetime
from django.db import migrations
import django.utils.timezone
from django.utils.timezone import utc
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20151018_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 5, 23, 47, 37, 131688, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 5, 23, 47, 41, 701500, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 5, 23, 47, 46, 629478, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 5, 23, 47, 51, 591637, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faction',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 5, 23, 47, 56, 265986, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faction',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 5, 23, 48, 5, 887544, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pgroup',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pgroup',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 5, 23, 48, 17, 535173, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 5, 23, 48, 22, 4880, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 5, 23, 48, 26, 577825, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
    ]