from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status')
        if status:
            return Task.objects.filter(status=status)
        return Task.objects.all()


class TaskDetail(APIView):
    def get(self, request, id):
        try:
            task = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

