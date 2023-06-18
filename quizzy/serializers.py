from rest_framework import serializers
from quizzy.models import Quiz, QuizResult, Answer, Notification, UserProfile, Category, Question
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# from djoser.serializers import UserSerializer

# class CustomUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'other_custom_fields')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
 
class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = UserProfile
            fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture','password')
            
#override TokenCreateView to use email instead of username

class CustomTokenCreateSerializer(TokenSerializer):
    username_field = 'email'

    def validate(self, attrs):
        password = attrs.get("password")
        user = authenticate(
            username=attrs.get("email"), password=password
        )
        if not user:
            msg = "Unable to log in with provided credentials."
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs   





class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    # answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = "__all__"

class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'
    
    #override create method
    
    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     print(category_data)
    #     category, _ = Category.objects.get_or_create(**category_data)
    #     quiz = Quiz.objects.create(
    #         category=category, **validated_data)
        
    #     return quiz


class QuizResultSerializer(serializers.ModelSerializer):
    # calling user serializer
    # user = UserSerializer()
    # quiz = QuizSerializer()

    class Meta:
        model = QuizResult
        fields = '__all__'
    
    # def create(self, validated_data):
    #     quiz_data = validated_data.pop('quiz')
    #     # cat, _ = Category.objects.get_or_create(**quiz_data['category']) 
    #     #add the company to the supervisor
    #     # quiz_data['category'] = cat 
    #     quiz, _ = Quiz.objects.get_or_create(**quiz_data)
    #     user_data = validated_data.pop('user')
    #     # user, _ = UserProfile.objects.get_or_create(**user_data)
    #     quiz_result = QuizResult.objects.create(
    #         quiz=quiz , **validated_data)
    #     return quiz_result


class NotificationSerializer(serializers.ModelSerializer):

    # user = UserSerializer()

    class Meta:
        model = Notification
        fields = '__all__'


