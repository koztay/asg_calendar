# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from cal import views
from asg.users import views as uviews
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'pgroups', views.PGroupViewSet)
router.register(r'factions', views.FactionViewSet)
router.register(r'slots', views.SlotViewSet)
router.register(r'entries', views.EntryViewSet)
router.register(r'users', uviews.UserViewSet)



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("asg.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^api/', include(router.urls)),
    url(r'^', include('cal.urls', namespace='cal')),
    url(r'^nested_admin/', include('nested_admin.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]

urlpatterns += [
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),
]
