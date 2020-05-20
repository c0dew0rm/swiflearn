from rest_framework import serializers
from .models import UserProfile, Class, ClassTaken, Question
from django.http import JsonResponse


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class ClassTakenSerializer(serializers.ModelSerializer):
    classid = serializers.ReadOnlyField(source='classTaken.id')
    className = serializers.ReadOnlyField(source='classTaken.classTitle')
    instructorName = serializers.ReadOnlyField(source='classTaken.instructorName')
    classQuestions = serializers.SerializerMethodField('getClassQuestions')

    class Meta:
        model = ClassTaken
        fields = ['classid', 'className', 'instructorName', 'classQuestions' ]

    def getClassQuestions(self, obj):
        questionList = []
        try:
            questions = Question.objects.filter(className=obj.classTaken)
            for question in questions:
                questionList.append(question.question)
            return questionList
        except:
            return


class ClassSerializer(serializers.ModelSerializer):
    class_question = QuestionSerializer(many=True, read_only=True)
    class_info = ClassTakenSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['classTitle', 'instructorName', 'class_question', 'class_info']


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    firstName = serializers.ReadOnlyField(source='user.first_name')
    lastName = serializers.ReadOnlyField(source='user.first_name')
    email = serializers.ReadOnlyField(source='user.first_name')
    user_student_class = ClassTakenSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'firstName', 'lastName', 'email', 'city', 'grade', 'board', 'user_student_class']
