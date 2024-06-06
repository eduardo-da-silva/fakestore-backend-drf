from django.db import models

from uploader.models import Image


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self) -> str:
        return f"{str(self.title)}"
