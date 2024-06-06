from rest_framework import serializers

from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects."""

    class Meta:
        model = Category
        fields = ("id", "name", "icon", "parent")
        read_only_fields = ("id",)
