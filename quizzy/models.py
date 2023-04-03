from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

import time


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    
    def __str__(self):
        return self.question


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    points = models.IntegerField(default=1)
    
    def __str__(self):
        return self.text

# modify user model to add profile picture


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(
    upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.username


class QuizResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    fastest_time = models.TimeField()
    
    


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(UserProfile)
    
    def __str__(self):
        return self.title
