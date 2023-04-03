from django.contrib import admin
from .models import Quiz, QuizResult, Answer, Notification

# Register your models here.


admin.site.register(Quiz)
admin.site.register(QuizResult)
admin.site.register(Answer)
admin.site.register(Notification)
