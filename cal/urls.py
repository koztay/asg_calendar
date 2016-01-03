from django.conf.urls import patterns, url
from cal.views import EventListView, EventDetailView


urlpatterns = patterns('',
                       url(r'^events/$', EventListView.as_view(), name='event-list'),
                       url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-detail')
                       )
