from rest_framework import serializers

from .models import Course
from .models import UserCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 


class CreateUserCourseSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
    )

    class Meta:
        model = UserCourse
        fields = ('id', 'user_id', 'course_id', 'state')
        read_only_fields = ['id']

    def create(self, validated_data):
        return UserCourse.objects.create(**validated_data)


class UodateUserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('state',)

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance