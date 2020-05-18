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
        return user.username

class Class(models.Model):
    classTitle = models.CharField(max_length=30, null=False, default=None, unique=True)
    instructorName = models.CharField(max_length=30, null=False, default=None)

    def __str__(self):
        return self.classTitle


class ClassTaken(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    classTaken = models.OneToOneField(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Question(models.Model):
    className = models.ForeignKey(Class, on_delete=models.CASCADE)
    question = models.CharField(max_length=30, null=False, default=None, unique=True)

    def __str__(self):
        return self.id