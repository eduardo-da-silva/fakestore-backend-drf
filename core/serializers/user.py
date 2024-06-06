from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "passage_id", "email", "name", "is_staff", "is_active")

