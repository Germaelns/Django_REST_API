from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import posts
from .serializers import *
from .models import Post


class PostApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
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
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            post = Post.objects.get(title=request.GET.get('title'))
            data = {
                "Title": post.title,
                "Content": post.content,
                "Author": post.author,
                "Likes": post.likes,
                "date": post.date
            }
            return Response(data, status=status.HTTP_200_OK)
        except posts.models.Post.DoesNotExist:
            data = "Post does not exist"
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        post = Post.objects.get(title=request.data['title'])

        if request.data['like'] == 1:
            post.likes += 1
            post.save()
            data = "Successful like adding"
        else:
            post.likes -= 1
            post.save()
            data = "Successful unlike adding"

        return Response(data, status=status.HTTP_200_OK)
