from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        if serializer.save():
            data = "User created successfully"
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = "User creation failed"
            return Response(data, status=status.HTTP_201_CREATED)

