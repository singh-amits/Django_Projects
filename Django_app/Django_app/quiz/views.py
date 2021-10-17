from django.shortcuts import get_object_or_404, render
from django.views.generic import  ListView
from django.views.decorators.cache import cache_control
from django.core.exceptions import  ImproperlyConfigured
from django.views.generic.edit import FormView
from django.shortcuts import render
from .forms import QuestionForm
from .models import Answer, Quiz, Category, UserAnswer, UserProgress, Question
import datetime



class CategoriesListView(ListView):
    """
    Lists all categories.
    """
    model = Category


class ViewQuizListByCategory(ListView):
    """
    Lists all quizzes in a certain category.
    """
    model = Quiz
    template_name = 'quiz/view_quiz_category.html'

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(
            Category,
            category=self.kwargs['category_name']
        )

        return super(ViewQuizListByCategory, self).\
            dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewQuizListByCategory, self)\
            .get_context_data(**kwargs)

        context['category'] = self.category
        return context

    def get_queryset(self):
        queryset = super(ViewQuizListByCategory, self).get_queryset()
        return queryset.filter(category=self.category)


class QuizTakeView(FormView):

    """
    Displays questions belonging to the respective quiz one by one.
    """

    form_class = QuestionForm
    template_name = 'quiz/question.html'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, slug=self.kwargs['quiz_name'])
        self.all_questions = self.get_all_questions()
        self.logged_in_user = self.request.user.is_authenticated

        if self.logged_in_user:    
            attempted = self.check_if_attempted(self.request)       
            if attempted:
                return render(self.request,"quiz/completed.html", {"quiz":self.quiz})  
            
            self.progress= UserProgress.objects.saved_progress(request.user, self.quiz) 
            self.question_set = self.remove_attempted_questions()
                                              
        return super(QuizTakeView, self).dispatch(request, *args, **kwargs)

    def check_if_attempted(self, request):
        """
        Check if the user has already attempted the quiz.
        """
        try:
            obj = UserProgress.objects.get(user=request.user, quiz=self.quiz, complete=True)
        except UserProgress.DoesNotExist:
            return False
        return (obj is not None)

    def get_all_questions(self):
        """
        Return all questions in a quiz
        """
        question_set = self.quiz.question_set.all() \
                                        .select_subclasses()

        question_set = [item.id for item in question_set]

        if len(question_set) == 0:
            raise ImproperlyConfigured('Question set of the quiz is empty. '
                                       'Please configure questions properly')  
              
        return question_set
    
    def remove_attempted_questions(self):
        """
        Returns list of questions for which the user hasn't given an answer yet.
        """
        answered = UserAnswer.objects.filter(user=self.progress.user, quiz=self.quiz)
        answered_list = [item.question.id for item in answered]
        question_set = [question for question in self.all_questions if question not in answered_list] 
        return question_set

    def get_first_question(self):
        """
        Returns the first question from set of all questions
        """
        if not self.question_set:
            return False

        first_question = self.question_set[0]
        question_id = first_question
        return Question.objects.get_subclass(id=question_id)

    def remove_first_question(self):
        """
        Removes the first question from set of all questions
        """
        if not self.question_set:
            return
        self.question_set.pop(0)
        self.progress.answered+=1
        self.progress.save()

    def get_max_questions(self):
        """
        Returns total no. of questions in the quiz
        """
        return len(self.all_questions)

    def answer_progress(self):
        """
        Returns the no. of questions answered from total questions in the quiz.
        """
        answered = int(self.progress.answered)
        total = self.get_max_questions()
        return answered, total

    def get_form(self, form_class=QuestionForm):
        """
        Gets the question form 
        """
        if self.logged_in_user:
            self.question = self.get_first_question()
            self.question_progress = self.answer_progress()
            self.minutes, self.seconds = self.progress.get_duration
        return form_class(**self.get_form_kwargs())

    def get_form_kwargs(self):
        """
        Gets the kwargs from forms
        """
        kwargs = super(QuizTakeView, self).get_form_kwargs()

        return dict(kwargs, question=self.question)

    def form_valid(self, form):
        """
        Check if valid data has been entered in form
        """
        if self.logged_in_user:
            self.form_valid_user(form)
            if self.get_first_question() is False:
                return self.final_result_user()
        self.request.POST = {}
        return super(QuizTakeView, self).get(self, self.request)

    def get_context_data(self, **kwargs):
        """
        Updates context data with recent information
        """
        context = super(QuizTakeView, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['quiz'] = self.quiz
        context['minutes'], context['seconds'] = self.progress.get_duration
        if hasattr(self, 'question_progress'):
            context['question_progress'] = self.question_progress
        return context

    def form_valid_user(self, form):
        """
        Checks whether answer was correct and increments score accordingly.
        """
        question = form._q_id  
        minutes = self.request.POST.get('minutes')
        seconds = self.request.POST.get('seconds')
        if form._mcq:
            guess = form.cleaned_data['answers']            
            is_correct = self.question.check_if_correct(guess)
            guess = Answer.objects.get(id=guess)
        else:
            guess = form.cleaned_data['answer']            
            is_correct = self.question.check_if_correct(question,guess)

        if is_correct is True:
            self.progress.add_to_score(form._mcq, question)
        #add to user answers
        self.progress.add_user_answer(self.question, guess, is_correct)
        self.progress.decrease_timer(minutes, seconds)
        self.remove_first_question()

    def final_result_user(self):
        """
        Displays final result after all questions have been attempted
        """
        results = {
            'quiz': self.quiz,
            'score': self.progress.get_current_score,
            'answered': self.progress.answered,
            'max_questions': self.get_max_questions(),
            'user_progress': self.progress,
        }

        self.progress.mark_quiz_complete()

        return render(self.request, 'quiz/result.html', results)


class AnswersListView(ListView):
    """
    Displays all answers given by user for respective questions and 
    whether they were correct or not.
    """
    model = UserAnswer
    template_name = "quiz/result_with_answers.html"

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.quiz_url = self.kwargs["quiz_name"]
        self.quiz = Quiz.objects.get(slug = self.quiz_url)
        user_progress = UserProgress.objects.get(user=self.user, quiz=self.quiz)
        if user_progress.end is None:
            user_progress.end = datetime.datetime.now()
        user_progress.complete = True
        user_progress.save()
        self.add_unattempted_questions()
        return super(AnswersListView, self).\
            dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(AnswersListView, self).get_queryset()        
        return queryset.filter(user=self.user, quiz=self.quiz)
    
    def add_unattempted_questions(self):
        """
        Adds to UserAnswer, questions left due to time.
        """
        question_set = self.quiz.question_set.all() \
                                        .select_subclasses()

        answered = UserAnswer.objects.filter(user=self.user, quiz=self.quiz)
        answered_list = [item.question.id for item in answered]
        unanswered = [question for question in question_set if question.id not in answered_list] 
        for question in unanswered:
            user_answer = UserAnswer(user=self.user, quiz=self.quiz , question=question, answer="", correct=False)
            user_answer.save()

class ProgressListView(ListView):
    """
    Displays the progress of user in all attempted quizes.
    Includes details such as marks earned and whether the 
    User has completed the quiz.
    """
    model = UserProgress
    template_name = "quiz/user_progress.html"

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(ProgressListView, self).\
            dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ProgressListView, self).get_queryset()
        return queryset.filter(user=self.user)