from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from core.models import Order, OrderItem


class OrderItemsSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.product.price * instance.quantity

    class Meta:
        model = OrderItem
        fields = ("product", "quantity", "total")
        depth = 1


class OrderSerializer(ModelSerializer):
    user = CharField(source="user.email", read_only=True)
    items = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "user", "status", "total", "items")


class OrderCreateSerializer(ModelSerializer):
    items = OrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = ("user", "items")
