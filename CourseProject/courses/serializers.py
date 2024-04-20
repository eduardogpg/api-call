from rest_framework import serializers

from .models import Course
from .models import UserCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 

