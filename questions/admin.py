from django.contrib import admin
from .models import Question, Answer
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('author', 'image', 'topic','the_question','question_type','created_at')
    search_fields = ('author', 'status','topic')
    list_filter = ('created_at', 'status', 'question_type')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer','created_at')
    search_fields = ('user',)
    list_filter = ('created_at',) 


