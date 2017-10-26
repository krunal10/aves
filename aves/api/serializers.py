from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer, UUIDField

from .models import Organization


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class OrganizationSerializer(HyperlinkedModelSerializer):
    organization_id = UUIDField(read_only=True)

    class Meta:
        model = Organization
        fields = ('organization_id', 'name', 'description', 'created_at',
                  'updated_at', 'user')
        depth = 2
