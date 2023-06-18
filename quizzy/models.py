from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

import time


class Category (models.Model):
    categ_id = models.AutoField(primary_key=True)
    categ_name = models.CharField(max_length=50, )
    categ_image = models.ImageField(upload_to='category_images', blank=True)
    categ_description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.categ_name

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category.categ_name
    

class Question(models.Model):
    
    id_question = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_image = models.ImageField(upload_to='question_images', blank=True)
    
    def __str__(self):
        return self.text
    


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    points = models.IntegerField(default=1)
    
    def __str__(self):
        return self.text

# modify user model to add profile picture


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(
    upload_to='profile_pictures', blank=True)
    #make user active 
    is_active = models.BooleanField(default=True)

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
