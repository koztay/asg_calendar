from django.contrib import admin
from .models import Event, Entry, Slot, Faction, PGroup
from nested_admin import NestedStackedInline, NestedAdmin


class SlotInline(NestedStackedInline):
    model = Slot
    extra = 0


class FactionInline(NestedStackedInline):
    model = Faction
    extra = 0
    inlines = [SlotInline, ]


class EventAdmin(NestedAdmin):
    model = Event
    inlines = [FactionInline, ]


admin.site.register(Event, EventAdmin)
admin.site.register(Entry)
admin.site.register(Slot)
admin.site.register(Faction)
admin.site.register(PGroup)
