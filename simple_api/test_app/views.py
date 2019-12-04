from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson
from .serializers import UserSerializer, LessonSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    paginate_by = 100


class LessonView(ListCreateAPIView):
    def get(self, request):
        lesson = Lesson.objects.all()
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)

    def post(self, request):
        lesson = LessonSerializer(data=request.data)
        if lesson.is_valid():
            lesson.save()
            return Response(lesson.data, status=status.HTTP_201_CREATED)
        return Response(lesson.errors, status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    def get(self, request):
        return Response({
            'messages': 'GET response'
        }, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({
            'messages': 'POST response'
        }, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response({
            'messages': 'PUT response'
        }, status=status.HTTP_202_ACCEPTED)

    def delete(self, request):
        return Response({
            'messages': 'DELETE response'
        }, status=status.HTTP_204_NO_CONTENT)