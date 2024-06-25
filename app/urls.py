from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from core.views import CategoryViewSet, OrderViewSet, ProductViewSet, UserViewSet
from uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"orders", OrderViewSet, basename="orders")
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
    path("api/media/", include(uploader_router.urls)),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
