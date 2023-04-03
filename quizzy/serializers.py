from rest_framework import serializers
from quizzy.models import Quiz, QuizResult, Answer, Notification, UserProfile
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

 
class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = UserProfile
            fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizResultSerializer(serializers.ModelSerializer):
    # calling user serializer
    user = UserSerializer()
    quiz = QuizSerializer()

    class Meta:
        model = QuizResult
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    # user = UserSerializer()

    class Meta:
        model = Notification
        fields = '__all__'
