from django.urls import path
from quizzy.views import QuizList, QuizDetail, QuizResultList, QuizResultDetail, NotificationList, NotificationDetail, AnswerList, AnswerDetail, UserList, UserDetail

urlpatterns = [
    path('quizzes/', QuizList.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizDetail.as_view(), name='quiz-detail'),
    path('quizresults/', QuizResultList.as_view(), name='quizresult-list'),
    path('quizresults/<int:pk>/', QuizResultDetail.as_view(),
         name='quizresult-detail'),
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(),
         name='notification-detail'),
    path('answers/', AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),



]
