from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.apis.PostCreate.serializers import PostCreateSerializer
from posts.apis.PostList.serializers import PostListSerializer


class PostCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_data = PostCreateSerializer(data=data)
        serializer_data.is_valid(
            raise_exception=True
        )
        post = Post.objects.create(
            **serializer_data.validated_data,
            owner=request.user
            )
        return Response(
            {
                "post": PostListSerializer(post).data
            }
        )