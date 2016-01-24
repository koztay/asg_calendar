# from django.shortcuts import render, render_to_response
from cal.models import Event, PGroup, Faction, Slot, Entry
from cal.serializers import EventSerializer, FactionSerializer, SlotSerializer
from cal.serializers import PGroupSerializer, EntrySerializer
from rest_framework import viewsets
from cal.permissions import IsOwnerOrReadOnly
from django.views.generic import ListView, DetailView
from django.utils import timezone


# API Views
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for events
    """
    queryset = Event.objects.all().order_by('datetime')
    serializer_class = EventSerializer

    def update(self, request, *args, **kwargs):
        self.methods = ('put', )
        self.permission_classes = (IsOwnerOrReadOnly, )
        return super(self.__class__, self).update(request, *args, **kwargs)


class PGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Player groups
    """
    queryset = PGroup.objects.all().order_by('name')
    serializer_class = PGroupSerializer


class FactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for factions
    """
    queryset = Faction.objects.all().order_by('event', 'name')
    serializer_class = FactionSerializer


class SlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint for slots
    """
    queryset = Slot.objects.all().order_by('faction', 'name')
    serializer_class = SlotSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for entries
    """
    queryset = Entry.objects.all().order_by('event', 'faction')
    serializer_class = EntrySerializer


#
# ---- Generic Django Views
#
class EventListView(ListView):
    queryset = Event.objects.filter(datetime__gte=timezone.now())
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
