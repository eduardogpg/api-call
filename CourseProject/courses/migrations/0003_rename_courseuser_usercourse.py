# Generated by Django 4.2.11 on 2024-04-19 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courseuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseUser',
            new_name='UserCourse',
        ),
    ]
