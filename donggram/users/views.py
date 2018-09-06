from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        # create_at 은 사용 불가하다 왜냐하면 created_at 은 부모클래스의 데이터인 date_joined의 역할이 있기때문

        serializer = serializers.ExploreUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)