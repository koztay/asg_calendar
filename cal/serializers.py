from rest_framework import serializers
from cal.models import Event, PGroup, Faction, Slot, Entry


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ('title', 'description', 'created_by', 'poster', 'datetime',
                  'starttime1', 'starttime2', 'starttime2', 'endtime1',
                  'endtime2', 'location', 'location_video', 'areamap', 'fps',
                  'ammo', 'terms', 'entry_fee', 'slot_limit', 'pyro',
                  'underage', 'rules', 'info', 'link'
                  )
        excluded_fields = ()


class PGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PGroup
        fields = ('name', 'logo', 'website', 'description')


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ('event', 'name')


class SlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slot
        fields = ('name')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('event', 'user', 'slot', 'faction')
