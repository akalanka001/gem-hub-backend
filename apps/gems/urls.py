from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GemListingViewSet

router = DefaultRouter()
router.register(r"gems", GemListingViewSet)  # Prefix for the URL

urlpatterns = [
    path("gems/by_owner/<uuid:owner_id>/", GemListingViewSet.as_view({"get": "get_by_owner"})),
    path("", include(router.urls)),
]
