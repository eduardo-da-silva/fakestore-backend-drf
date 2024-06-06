from django.db import models

from .product import Product


class Order(models.Model):
    class Meta:
        ordering = ("-created_at",)

    class Status(models.IntegerChoices):
        CART = 0, "Cart"
        PENDING = 1, "Pending"
        COMPLETED = 2, "Completed"
        CANCELLED = 3, "Cancelled"

    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey("core.User", on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status.choices, default=Status.CART)

    def __str__(self):
        return f"Order {self.id} ({self.status})"  # pylint: disable=no-member


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order} - {self.product.title}"  # pylint: disable=no-member
