from rest_framework.viewsets import ModelViewSet

from core.models import Order
from core.serializers import OrderSerializer, OrderCreateSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()  # pylint: disable=E1101
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return OrderCreateSerializer
        return super().get_serializer_class()
