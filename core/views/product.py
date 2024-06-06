from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core.models import Product
from core.serializers.product import ProductSerializer, ProductDetailSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  # pylint: disable=no-member
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__id"]

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return ProductDetailSerializer
        return ProductSerializer
