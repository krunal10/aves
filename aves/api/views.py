from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import Group, User
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Organization
from .serializers import GroupSerializer, OrganizationSerializer, UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
