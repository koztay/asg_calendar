# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from django_extensions.db.models import TimeStampedModel

class Event(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name='tytuł')
    description = models.TextField(verbose_name='opis', blank=True)
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
    fps = models.TextField(verbose_name='fps', blank=True)
    ammo = models.TextField(verbose_name='amunicja', blank=True)
    terms = models.TextField(verbose_name='regulamin', blank=True)
    entry_fee = models.TextField(verbose_name='wpisowe', blank=True)
    slot_limit = models.PositiveIntegerField(
        verbose_name='limit miejsc', blank=True, null=True, default=None)
    pyro = models.BooleanField(verbose_name='pirotechnika', default=False)
    underage = models.BooleanField(verbose_name='nieletni', default=False)
    rules = models.TextField(verbose_name='zasady gry', blank=True)
    info = models.TextField(verbose_name='wiecej informacji',
                            blank=True)
    link = models.URLField(blank=True)
    is_open = models.BooleanField(default=True, verbose_name='otwarte')

    class Meta:
        verbose_name = 'wydarzenie'
        verbose_name_plural = 'wydarzenia'

    def __str__(self):
        return self.title

    @property
    def signed_up_users(self):
        users = []
        for faction in self.factions.all():
            users.extend(faction.users.all())
        return users

    def user_can_sign_up(self, user):
        try:
            slot_limit_exceeded = len(self.signed_up_users) > self.slot_limit
        except TypeError:
            slot_limit_exceeded = False
        if user not in self.signed_up_users and self.is_open and not slot_limit_exceeded:
            return True
        return False

    # def attrs(self):
    #     # for attr, value in self._meta.get_fields():
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr, value


class PGroup(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name='nazwa')
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    website = models.URLField(null=True, blank=True, verbose_name='strona www')
    description = models.TextField(null=True, blank=True, verbose_name='opis')

    class Meta:
        verbose_name = 'grupa'
        verbose_name_plural = 'grupy'

    def __str__(self):
        return self.name


class Faction(TimeStampedModel):
    event = models.ForeignKey(Event, related_name='factions')
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='cal.Entry',
                                  related_name='factions', verbose_name='użytkownicy')

    class Meta:
        verbose_name = 'frakcja'
        verbose_name_plural = 'frakcje'

    def __str__(self):
        return '{0} - {1}'.format(self.event, self.name)

    def get_non_slot_players(self):
        return self.entries.filter(slot=None)


class Slot(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name='nazwa',
                            blank=False, null=False)
    # event = models.ForeignKey(Event)
    faction = models.ForeignKey(Faction)

    class Meta:
        verbose_name = "slot"
        verbose_name_plural = 'sloty'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.faction.event)


class Entry(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entries',
                             verbose_name='użytkownik')
    slot = models.OneToOneField(Slot, blank=True, null=True)
    faction = models.ForeignKey(Faction, related_name='entries', blank=False, null=False)

    class Meta:
        verbose_name = 'zapis'
        verbose_name_plural = 'zapisy'
        ordering = ['pk']

    def __str__(self):
        return "{0} - {1}".format(self.user, self.slot)
