from django.urls import path
from .views import PostListCreateView, PostDetail, PostLike
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('posts', PostListCreateView.as_view()),
    path('posts/<int:id>', PostDetail.as_view()),
    path('posts/<int:id>/like', PostLike.as_view())
]

