from django.urls import path

from posts.apis import PostCreateAPIView, PostDetailAPIView, PostListAPIView
from posts import views


urlpatterns = [
    path('all/', PostListAPIView.as_view(), name="post_list"),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),

    path('hello/', views.HelloWorldView.as_view(), name="hello_world")
]