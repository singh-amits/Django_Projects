from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


app_name = 'quiz'
urlpatterns = [
    path('category/', login_required(views.CategoriesListView.as_view()), name='quiz_category_list_all'),
    path('category/<str:category_name>/', login_required(views.ViewQuizListByCategory.as_view()), name='quiz_category_list_matching'),
    path('<str:quiz_name>/take/', login_required(views.QuizTakeView.as_view()), name='quiz_question'),
    path('<str:quiz_name>/results/', login_required(views.AnswersListView.as_view()), name='quiz_results'),
    path('progress/', login_required(views.ProgressListView.as_view()), name='user_progress'),
    
    
]