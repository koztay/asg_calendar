from django.db import models
# from datetime import datetime
from django.conf import settings
from django.utils import timezone
from location_field.models.plain import PlainLocationField
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='tytuł')
    description = models.TextField(verbose_name='opis', null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   blank=True, verbose_name='stworzone przez')
    poster = models.ImageField(upload_to='posters', blank=True, null=True,
                               verbose_name='zdjecie')
    datetime = models.DateTimeField(default=timezone.now,
                                    verbose_name='data i czas')
    starttime1 = models.TimeField(verbose_name='rozgrywki1')
    starttime2 = models.TimeField(verbose_name='rozgrywki2')
    endtime1 = models.TimeField(verbose_name='koniec1')
    endtime2 = models.TimeField(verbose_name='koniec2')
    location = PlainLocationField(zoom=14, default='53.43,14.56')
    location_video = models.URLField(verbose_name='miejsce zbiorki (video)',
                                     blank=True, null=True)
    areamap = models.FileField(verbose_name='mapa', null=True, blank=True)
    fps = models.TextField(verbose_name='fps', null=True, blank=True)
    ammo = models.TextField(verbose_name='amunicja', null=True, blank=True)
    terms = models.TextField(verbose_name='regulamin', null=True, blank=True)
    entry_fee = models.TextField(verbose_name='wpisowe', null=True, blank=True)
    slot_limit = models.PositiveIntegerField(
        verbose_name='limit miejsc', blank=True, null=True, default=None)
    pyro = models.BooleanField(verbose_name='pirotechnika', default=False)
    underage = models.BooleanField(verbose_name='nieletni', default=False)
    rules = models.TextField(verbose_name='zasady gry', null=True, blank=True)
    info = models.TextField(verbose_name='wiecej informacji',
                            null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'wydarzenie'
        verbose_name_plural = 'wydarzenia'

    def __str__(self):
        return self.title


class PGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name='nazwa')
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    website = models.URLField(null=True, blank=True, verbose_name='strona www')
    description = models.TextField(null=True, blank=True, verbose_name='opis')

    class Meta:
        verbose_name = 'grupa'
        verbose_name_plural = 'grupy'

    def __str__(self):
        return self.name


class Faction(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'frakcja'
        verbose_name_plural = 'frakcje'

    def __str__(self):
        return '{0} - {1}'.format(self.event, self.name)


class Slot(models.Model):
    name = models.CharField(max_length=200, verbose_name='nazwa',
                            blank=False, null=False)
    # event = models.ForeignKey(Event)
    faction = models.ForeignKey(Faction)

    class Meta:
        verbose_name = "slot"
        verbose_name_plural = 'sloty'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.faction.event)


class Entry(models.Model):
    event = models.ForeignKey(Event, blank=False, null=False,
                              verbose_name='wydarzenie')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='użytkownik')
    slot = models.OneToOneField(Slot, blank=True, null=True)
    faction = models.ForeignKey(Faction, blank=True, null=True)

    class Meta:
        verbose_name = 'zapis'
        verbose_name_plural = 'zapisy'
        ordering = ['pk']

    def __str__(self):
        return "{0} - {1} | {2}".format(self.user, self.slot, self.event)
