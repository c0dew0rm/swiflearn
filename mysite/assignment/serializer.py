from rest_framework import serializers
from .models import UserProfile, Class, ClassTaken, Question

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = []

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class ClassTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTaken
        fields = ['classTaken',]


class ClassSerializer(serializers.ModelSerializer):
    class_question = QuestionSerializer(many=True, read_only=True)
    class_info = ClassTakenSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['classTitle', 'instructorName', 'class_question', 'class_info']


class UserProfileSerializer(serializers.ModelSerializer):
    user_student_class = ClassTakenSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ['age', 'city', 'grade', 'board', 'user_student_class']
