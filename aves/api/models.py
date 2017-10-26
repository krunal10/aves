import uuid

from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    organization_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (("name", "user"))
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        app_label = 'api'
        db_table = 'organization'

    def __unicode__(self):
        return self.name
