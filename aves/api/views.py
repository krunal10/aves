from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import Organization
from .serializers import UserSerializer, GroupSerializer, \
    OrganizationSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
