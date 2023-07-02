# using querysets
from http.client import ResponseNotReady
from .models import Quiz, QuizResult, Answer, Notification, UserProfile, Category, Question
from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import QuizSerializer, QuizResultSerializer, QuestionSerializer, AnswerSerializer, NotificationSerializer, UserSerializer, CategorySerializer
# importing permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
from .serializers import CustomTokenCreateSerializer
from rest_framework.authtoken.models import Token
#import Response
from rest_framework.response import Response
from djoser import views as djoser_views

from rest_framework import status
from djoser.conf import settings


    
    


class UserCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = UserProfile.objects.create_user(**serializer.validated_data)
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(djoser_views.TokenCreateView):
    serializer_class = CustomTokenCreateSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryQuizDetail(APIView):
    
    def get(self, request, *args, **kwargs):
       quiz = Quiz.objects.filter(category=kwargs['pk']).first()
       serializer = QuizSerializer(quiz)
       return Response(serializer.data)


# only authenticated admin users can add and modify quizzes
class QuizList(ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]



class QuizDetail(RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class QuizQuestionList(APIView):

    
    def get(self, request, *args, **kwargs):
       questions = Question.objects.filter(quiz=kwargs['pk'])
       serializer = QuestionSerializer(questions, many=True, context={'request': request})
       return Response(serializer.data)  
   
   
        




class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated]
    
    #override the post method to accept array of question objects
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            for question in request.data:
                serializer = QuestionSerializer(data=question)
                if serializer.is_valid():
                    serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return super().post(request, *args, **kwargs)
        
        
    

class QuestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated]


class QuestionDifficultyView(APIView):
    
    def get(self, request, *args, **kwargs):
       questions = Question.objects.filter(quiz=kwargs['pk'], difficulty=kwargs['difficulty'])
       serializer = QuestionSerializer(questions, many=True, context={'request': request})
       return Response(serializer.data)


class QuizAnswersView(APIView):
    def get(self, request, pk):
        answers = Answer.objects.filter(question__quiz=pk)
        serialized_answers = AnswerSerializer(answers, many=True)
        return Response(serialized_answers.data)


# only authenticated admin users can add and modify answers
class AnswerList(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class AnswerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


# only authenticated users can view, add and modify quiz results

class QuizResultList(ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer


class QuizResultDetail(RetrieveUpdateDestroyAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
    # permission_classes = [IsAuthenticated]
    #override post method to get user id from token and save it to the quiz result
    # def post(self, request, *args, **kwargs):
    #     token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    #     user = Token.objects.get(key=token).user
    #     request.data['user'] = user.id
    #     return super().post(request, *args, **kwargs)   


# only authenticated admin users can view, add and modify notifications

class NotificationList(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class NotificationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

# user views


class UserList(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

