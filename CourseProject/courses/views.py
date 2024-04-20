from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer

class CourseListView(APIView):
    def get(self, reequest, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

class CourseUpdatePublishView(APIView):
    def put(self, request, pk, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        10 / 0
        if course:
            course.published_at = timezone.now()
            course.save()

            serializer = CourseSerializer(course)
            return Response(serializer.data)

        else:
            return Response(status=404)