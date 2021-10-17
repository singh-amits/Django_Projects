from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
from .models import Quiz, Category, Question ,UserProgress, UserAnswer, OnlyAnswer, QuestionOne, MCQQuestion, MCQAnswer
from django.utils.translation import ugettext_lazy as _

class AnswerInline(admin.StackedInline):
    """
    Add answers from question page itself
    """
    model = OnlyAnswer
    max_num = 1
 
class QuestonOneAdmin(admin.ModelAdmin):
    #display and filter settings
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category',
               'quiz', 'marks')

    search_fields = ('content',)
    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]

class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []

    #allow users to select multiple questions at once from quiz page
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    #display and filter settings
    form = QuizAdminForm

    list_display = ('title', 'category', )
    list_filter = ('category',)
    search_fields = ( 'category', )

class UserProgressAdmin(admin.ModelAdmin):
    #display and filter settings
    list_display = ('user', 'quiz', 'start', 'end')
    list_filter = ('user','quiz',)

class UserAnswerAdmin(admin.ModelAdmin):
    #display and filter settings
    list_display = ('user', 'quiz', 'question', )
    list_filter = ('user','quiz',)

class MCQAnswerInline(admin.TabularInline):
    """
    Add answers from question page itself
    """
    model = MCQAnswer

class MCQuestionAdmin(admin.ModelAdmin):
    #display and filter settings
    list_display = ('content', 'category', )
    list_filter = ('category',)
    fields = ('content', 'category',
               'quiz', 'answer_order','marks')

    search_fields = ('content',)
    filter_horizontal = ('quiz',)

    inlines = [MCQAnswerInline]


admin.site.register(MCQQuestion, MCQuestionAdmin)
admin.site.register(QuestionOne,QuestonOneAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category)
admin.site.register(UserProgress, UserProgressAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)