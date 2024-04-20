from django.db import models
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    published_by = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class UserCourse(models.Model):
    
    class Status(models.IntegerChoices):
        CREATED = 0, _('Creado')
        COMPLETED = 1, _('Completado')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField()
    state = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'