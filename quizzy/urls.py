from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='catigories-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='catigories-detail'),
    path('categories/<int:pk>/quiz', views.CategoryQuizDetail.as_view(), name='Category_quiz_detail'),
    path('quizzes/', views.QuizList.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', views.QuizDetail.as_view(), name='quiz-detail'),
    path('quizzes/<int:pk>/questions/', views.QuizQuestionList.as_view(), name='quiz-question-list'),
    path('quizresults/', views.QuizResultList.as_view(), name='quizresult-list'),
    path('quizresults/<int:pk>/', views.QuizResultDetail.as_view(),
         name='quizresult-detail'),
    path('notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', views.NotificationDetail.as_view(),
         name='notification-detail'),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('questions/<int:pk2>/answers/', views.QuestionAnswerList.as_view(), name='question-answer-list'),
    path('answers/', views.AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>/', views.AnswerDetail.as_view(), name='answer-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('login/',views.LoginView.as_view(),name='login'),
    #UserCreateView
     path('register/',views.UserCreateView.as_view(),name='register'),
   



]
