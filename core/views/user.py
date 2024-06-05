from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import TokenAuthentication
from core.serializers.user import AuthSerializer

class AuthTokenView(APIView):
    authentication_classes = [TokenAuthentication]

    @staticmethod
    def post(request):
        user = request.user
        data = AuthSerializer(data=user).data
        return Response(data, status=status.HTTP_200_OK)
    