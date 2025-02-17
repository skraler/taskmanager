from django.urls import path
from .views import TaskListCreateView, TaskDetail
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('tasks', TaskListCreateView.as_view()),
    path('tasks/<int:id>', TaskDetail.as_view())
]
