from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return f"{str(self.name)}"
