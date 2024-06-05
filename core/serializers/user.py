from rest_framework.serializers import ModelSerializer, Serializer

from core.models import User


class AuthSerializer(Serializer):
    id: str
    passage_id: str
    auth_status: str

    def create(self, validated_data):
        validated_data['auth_status'] = "success"
        return self.create(validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
