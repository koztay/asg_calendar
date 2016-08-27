from django.conf import settings
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from django_extensions.db.models import TimeStampedModel
from django.core.exceptions import ValidationError


def validate_slot_number(value):
    try:
        faction = Faction.objects.get(id=value)
        if faction.event.slot_limit_reached():
            raise ValidationError(
                    'Przekroczono limit miejsc',
                    )
    except:
        pass


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

    rule_fields_names = ['fps', 'ammo', 'terms', 'entry_fee', 'rules', 'info']

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

    def slot_limit_reached(self):
        try:
            slot_limit_exceeded = len(self.signed_up_users) >= self.slot_limit
            if slot_limit_exceeded:
                return True
            return False
        except TypeError:
            return False

    def user_can_sign_up(self, user):
        if user.is_anonymous() or self.slot_limit_reached() or not self.is_open or \
                user in self.signed_up_users:
            return False
        return True

    # generator iterujacy po liscie nazw pol i zwracajacy pare: nazwa pola, wartosc pola
    def get_rule_fields(self):
        for field_name in self.rule_fields_names:
            yield self._meta.get_field(field_name).verbose_name, getattr(self, field_name)

    # properties potrzebne do wyświetlania mapy z lokalizacją
    @property
    def location_lat(self):
        return self.get_location_coordinates()[0]

    @property
    def location_lng(self):
        return self.get_location_coordinates()[1]

    def get_location_coordinates(self):
        return tuple(map(float, self.location.split(',')))


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
    faction = models.ForeignKey(Faction)

    class Meta:
        verbose_name = "slot"
        verbose_name_plural = 'sloty'

    def __str__(self):
        return '{0} - {1} | {2}'.format(self.name, self.faction.event, self.faction)


class Entry(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entries',
                             verbose_name='użytkownik')
    slot = models.OneToOneField(Slot, blank=True, null=True)
    faction = models.ForeignKey(Faction, related_name='entries', blank=False, null=False,
                                validators=[validate_slot_number])

    class Meta:
        verbose_name = 'zapis'
        verbose_name_plural = 'zapisy'
        ordering = ['pk']

    def __str__(self):
        return "{0} - {1} | {2}".format(self.user, self.slot, self.faction)
