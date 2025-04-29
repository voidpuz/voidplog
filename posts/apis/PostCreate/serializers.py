from rest_framework import serializers


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    cover = serializers.ImageField(required=False)