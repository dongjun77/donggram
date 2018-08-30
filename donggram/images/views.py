from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
# Create your views here.

class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # 파이썬 모델

        serializer = serializers.ImageSerializer(all_images, many=True) # 가지고온 파이썬 이미지 모델들을 json 모델로 변경해준다

        return Response(data=serializer.data)

class ListAllComments(APIView):

    def get(self, request, format=None):

        user_id = request.user.id

        all_comments = models.Comment.objects.filter(creator=user_id)

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)

class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)