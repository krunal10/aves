from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import GroupViewSet, OrganizationViewSet, UserViewSet

schema_view = get_swagger_view(title="Aves API", url="http://aves:8000/")

router = routers.DefaultRouter()
router.register(r"organizations", OrganizationViewSet)
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [url(r"^$", schema_view), url(r"^api/", include(router.urls))]
