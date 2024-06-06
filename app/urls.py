from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from core.views import CategoryViewSet, ProductViewSet, UserViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]
