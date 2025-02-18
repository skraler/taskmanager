from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(APIView):
    @staticmethod
    def get(request: object, id: int) -> object:
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(task)
        return Response(serializer.data)

    @staticmethod
    def put(request: object, id: int) -> object:
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, id: int) -> object:
        try:
            task = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'detail': 'Пост удален'}, status=status.HTTP_200_OK)


class PostLike(APIView):
    @staticmethod
    def add_like_to_post(request: object, id_post: int) -> object:
        try:
            post = Post.objects.get(pk=id_post)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.likes += 1
        post.save()
        return Response({'detail': 'Лайк добавлен'}, status=status.HTTP_200_OK)

    @staticmethod
    def delete_like_on_post(request: object, id_post: int) -> object:
        try:
            post = Post.objects.get(pk=id_post)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if post.likes > 0:
            post.likes -= 1
            post.save()
            return Response({'detail': 'Лайк удален'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Невозможно удалить лайк'}, status=status.HTTP_400_BAD_REQUEST)


def main_page(request):
    return render(request, 'index.html')
