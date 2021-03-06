from django.contrib import admin
from django.db import models
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date', 'was_published_recently')
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
