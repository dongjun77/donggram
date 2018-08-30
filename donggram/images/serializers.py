from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__' # like의 필드는 creator와 image가 있다.
class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = ( # 구체적으로 원하는 필드만 가져온다
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes',
        )
