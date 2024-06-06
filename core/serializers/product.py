from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Product


class ProductSerializer(ModelSerializer):
    image_attachment_key = SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),  # pylint: disable=no-member
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Product
        fields = ("id", "title", "description", "category", "price", "stock", "image", "image_attachment_key")
        read_only_fields = ("id", "image")


class ProductDetailSerializer(ModelSerializer):
    category = CharField(source="category.name")
    image = ImageSerializer(required=False)

    class Meta:
        model = Product
        fields = ("id", "title", "description", "category", "price", "stock", "image")
