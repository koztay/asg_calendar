from django.contrib import admin
from .models import Event, Entry, Slot, Faction, PGroup
# Register your models here.


admin.site.register(Event)
admin.site.register(Entry)
admin.site.register(Slot)
admin.site.register(Faction)
admin.site.register(PGroup)
