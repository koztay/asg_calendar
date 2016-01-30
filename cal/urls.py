from django.conf.urls import patterns, url
from cal.views import EventListView, EventDetailView, EntryCreateView


urlpatterns = patterns('',
                       url(r'^events/$', EventListView.as_view(), name='event-list'),
                       url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-detail'),
                       url(r'^events/(?P<pk>\d+)/signup/f(?P<faction_id>\d+)s(?P<slot_id>\d+)/$',
                           EntryCreateView.as_view(), name='entry_create'),
                       )
