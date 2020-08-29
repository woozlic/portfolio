from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [('Текст Вопроса', {'fields':['question_text']}),\
                 ('Информация о дате', {'fields':['pub_date']})]
    inlines = [ChoiceInLine]
# Register your models here.
admin.site.register(Question, QuestionAdmin)