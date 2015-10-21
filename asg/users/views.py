# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import User

from rest_framework import viewsets, mixins
from .serializers import UserSerializer
# from .permissions import IsUser
# from rest_framework.permissions import IsAdminUser, IsAuthenticated


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):

        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def update(self, request, *args, **kwargs):
    #     self.methods = ('put', )
    #     self.permission_classes = (IsUser, )
    #     return super(self.__class__, self).update(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     self.methods = ('post', )
    #     self.permission_classes = (IsAdminUser, )
    #     return super(self.__class__, self).update(request, *args, **kwargs)
