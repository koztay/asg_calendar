# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='stworzone przez', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='event',
            field=models.ForeignKey(verbose_name='wydarzenie', to='cal.Event'),
        ),
        migrations.AddField(
            model_name='entry',
            name='faction',
            field=models.ForeignKey(to='cal.Faction', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='slot',
            field=models.OneToOneField(to='cal.Slot', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(verbose_name='użytkownik', to=settings.AUTH_USER_MODEL),
        ),
    ]
