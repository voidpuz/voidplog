from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.apis.PostList.serializers import PostListSerializer


class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({"posts": PostListSerializer(posts, many=True).data})