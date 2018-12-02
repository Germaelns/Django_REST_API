from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_post(request):
    post = request.data
    post['user_id'] = request.user.id
    post['author'] = request.user.first_name + ' ' + request.user.last_name
    serializer = PostSerializer(data=post)
    serializer.is_valid(raise_exception=True)
    try:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        data = "Please post correct data"
        return Response(data, status=status.HTTP_409_CONFLICT)
