from rest_framework import serializers
from cal.models import Event, PGroup, Faction, Slot, Entry


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ('url', 'title', 'description', 'owner', 'poster', 'datetime',
                  'starttime1', 'starttime2', 'starttime2', 'endtime1',
                  'endtime2', 'location', 'location_video', 'areamap', 'fps',
                  'ammo', 'terms', 'entry_fee', 'slot_limit', 'pyro',
                  'underage', 'rules', 'info', 'link'
                  )
        excluded_fields = ()


class PGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PGroup
        fields = ('url', 'name', 'logo', 'website', 'description')


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ('url', 'event', 'name')


class SlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slot
        fields = ('url', 'name', 'faction')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('url', 'event', 'user', 'slot', 'faction')
