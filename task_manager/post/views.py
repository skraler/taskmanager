from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(APIView):

    def get(self, request: object, id: object) -> object:
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(task)
        return Response(serializer.data)

    def put(self, request: object, id: int) -> str:
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'detail': 'Пост удален'}, status=status.HTTP_200_OK)


class PostLike(APIView):
    def post(self, request, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.likes += 1
        post.save()
        return Response({'detail': 'Лайк добавлен'}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if post.likes > 0:
            post.likes -= 1
            post.save()
            return Response({'detail': 'Лайк удален'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Невозможно удалить лайк'}, status=status.HTTP_400_BAD_REQUEST)
