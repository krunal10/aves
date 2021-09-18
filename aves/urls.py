from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

version = "aves/v1/"
urlpatterns = [
    url(r"^" + version + "admin/", admin.site.urls),
    url(r"^" + version, include("api.urls", namespace="api")),
]
