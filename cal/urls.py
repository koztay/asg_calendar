from django.conf.urls import url, include
from rest_framework import routers
from cal import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'pgroups', views.PGroupViewSet)
router.register(r'factions', views.FactionViewSet)
router.register(r'slots', views.FactionViewSet)
router.register(r'entries', views.EntryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
