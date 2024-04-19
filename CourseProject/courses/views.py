from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, UserCourse

from .serializers import CourseSerializer
from .serializers import CreateUserCourseSerializer
from .serializers import UodateUserCourseSerializer

class CourseListView(APIView):
    def get(self, reequest, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

class UserCourseCreateUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserCourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, *args, **kwargs):
        user_course = UserCourse.objects.get(pk=kwargs.get('pk'))
        serializer = UodateUserCourseSerializer(user_course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)