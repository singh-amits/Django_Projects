from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.urls import reverse
import datetime
import re
import uuid

#settings to order options in mcqs
ANSWER_ORDER_OPTIONS = (
    ('content', 'Content'),
    ('none', 'None'),
    ('random', 'Random')
)

class CategoryManager(models.Manager):
    """
    Model manager for category model.
    removes whitespace and adds hifen(-) from title and changes it to lower case.
    """
    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category


class Category(models.Model):
    """
    Category model.
    Each category contains one or more quizzes.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=250,
        unique=True, )


    objects = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category


class Quiz(models.Model):
    """
    Stores details about a quiz.
    Url is a slug to be appended in the browser for given quiz.
    Each quiz belongs to one category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=60, blank=False)

    slug = models.SlugField(
        max_length=60, blank=False,
        unique=True,
        help_text=_("a user friendly url"),
        verbose_name=_("user friendly url"))
    duration = models.DurationField(null=True, blank=True)
    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name=_("Category"), on_delete=models.CASCADE)


    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        #format slug
        self.slug = re.sub('\s+', '-', self.slug).lower()

        self.slug = ''.join(letter for letter in self.slug if
                           letter.isalnum() or letter == '-')        

        super(Quiz, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")

    def __str__(self):
        return self.title

    def get_questions(self):
        #returns all questions of the quiz
        return self.question_set.all().select_subclasses()

    @property
    def get_max_questions(self):
        return self.get_questions().count()


class Question(models.Model):

    """
    Base class for Question
    Marks is the weightage for the respective question
    Each question can be in one or more quizzes.
    Every question has one category.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ManyToManyField(Quiz,
                                  verbose_name=_("Quiz"),
                                  blank=True)

    category = models.ForeignKey(Category,
                                 verbose_name=_("Category"),
                                 blank=True,
                                 null=True, on_delete=models.CASCADE)


    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the question text that "
                                           "you want displayed"),
                               verbose_name=_('Question'))

    marks = models.IntegerField(default=0,verbose_name='marks')

    objects = InheritanceManager()

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['category']

    def __str__(self):
        return self.content


class Answer(models.Model):
    """
    Base class for Answer
    """
    content = models.CharField(max_length=1000,
                                null=False,
                               blank=False,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")

    def __str__(self):
        return self.content
    
    objects = InheritanceManager()

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"



class MCQQuestion(Question):
    """
    Derived class for MCQs.
    answer_order determines the order of the options for displaying
    to the user.
    """

    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text="The order in which multichoice \
                    answer options are displayed \
                    to the user",
        verbose_name="Answer Order")

    def check_if_correct(self, guess):
        """
        Checks if guessed answer is correct
        """
        answer = MCQAnswer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        """
        Orders the options of each question as specified.
        """
        if self.answer_order == 'content':
            return queryset.order_by('content')
        if self.answer_order == 'random':
            return queryset.order_by('?')
        if self.answer_order == 'none':
            return queryset.order_by('None')

    def get_answers(self):
        #returns ordered answers
        return self.order_answers(MCQAnswer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(MCQAnswer.objects.filter(question=self))]

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"


class MCQAnswer(Answer):
    """
    Derived class for multiple-choice answers.
    correct indicates whether the given option is correct for linked question.
    """
    question = models.ForeignKey(MCQQuestion, verbose_name='Question', on_delete=models.CASCADE)

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?",
                                  verbose_name="Correct")


class QuestionOne(Question):
    """
    Derived class for one word questions
    """

    def check_if_correct(self, q, ans):
        """
        Checks whether the answer is correct.
        """
        answer = OnlyAnswer.objects.get(question=q)
        cleaned_guess = (ans.strip()).lower()
        if answer.content == cleaned_guess:
            return True
        else:
            return False

    def get_answers_list(self):
        return False
    
    def get_answers(self):
        return False


    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "One answer Question"
        verbose_name_plural = "One answer Questions"


class OnlyAnswer(Answer):
    """
    Derived class for one word answers
    """
    question = models.ForeignKey(QuestionOne, verbose_name='Question', on_delete=models.CASCADE)
    
class UserAnswer(models.Model):
    """
    Used to score the answers given by the user for a particular
    question of a given quiz.
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name=_("Questions"), on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, null=False, blank=True, verbose_name=_("Answers"))
    correct = models.BooleanField(default=False, blank=False)

    class Meta:
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"
    

class UserProgressManager(models.Manager):

    """
    Model manager for UserProgress model.
    saved_progress checks for existing progress object and return it.
    If not, it creates and returns new userprogress object
    """

    def new_progress(self, user, quiz):      
        new_progress = self.create(user=user,
                                  quiz=quiz,                                                              
                                  score=0,
                                  duration = quiz.duration,
                                  complete=False,)
        return new_progress

    def saved_progress(self, user, quiz):
        try:
            progress = self.get(user=user, quiz=quiz, complete=False)
        except UserProgress.DoesNotExist:
            progress = self.new_progress(user, quiz)    
        return progress

class UserProgress(models.Model):
    """
    Used to store the progress of logged in users sitting a quiz.
    Used to score the progress of user in a particular quiz
    Score is the marks a user has obtained so far.
    Answered is the no. of questions the user and attempted.
    Complete is a boolean field indicating whether or not the
    user has attempted all questions in the respective quiz
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quiz"), on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)
    start = models.DateTimeField(auto_now_add=True,verbose_name=_("Start"))
    end = models.DateTimeField(null=True, blank=True, verbose_name=_("End"))
    complete = models.BooleanField(default=False)
    answered = models.IntegerField(default=0)  
    objects = UserProgressManager()
    
    
    def add_to_score(self, mcq, question):
        """
        checks type of question and increments score
        """
        if mcq:
            question_obj = MCQQuestion.objects.get(id=question)
        else:
            question_obj = QuestionOne.objects.get(id=question)
        self.score += int(question_obj.marks)
        self.save()

    @property
    def get_current_score(self):
        return self.score

    @property
    def get_duration(self):
        """
        Returns remaining time in minutes and seconds
        """
        seconds = self.duration.total_seconds()
        mins, secs = divmod(seconds, 60)
        return int(mins), int(secs)

    def decrease_timer(self, mins, secs):
        """
        Updates time remaining
        """
        self.duration = datetime.timedelta(minutes=int(mins), seconds=int(secs))

    def mark_quiz_complete(self):
        """
        Marks quiz as completed to prevent further attempts.
        """
        self.end = now()
        self.complete=True
        self.save()

   
    def add_user_answer(self, question, guess, correct):
        """
        Adds answer submitted by user to the useranser model
        """
        user_answer = UserAnswer()
        user_answer.user = self.user
        user_answer.quiz = self.quiz
        user_answer.question = question
        user_answer.answer = guess
        user_answer.correct = correct
        user_answer.save()

    

    class Meta:
        verbose_name = "User Progress"
        verbose_name_plural = "User Progress"
    
