from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=30, null=False, default=None)
    grade = models.CharField(max_length=30, null=False, default=None)
    board = models.CharField(max_length=30, null=False, default=None)

    def __str__(self):
        return self.user.username


class Class(models.Model):
    classTitle = models.CharField(max_length=30, null=False, default=None, unique=True)
    instructorName = models.CharField(max_length=30, null=False, default=None)

    def __str__(self):
        return self.classTitle


class ClassTaken(models.Model):
    user = models.ForeignKey(UserProfile, related_name='user_student_class', on_delete=models.CASCADE)
    classTaken = models.ForeignKey(Class, related_name='class_info', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'classTaken',)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    className = models.ForeignKey(Class, related_name='class_question', on_delete=models.CASCADE)
    question = models.TextField(max_length=500, null=False, default=None)

    def __str__(self):
        return str(self.id)