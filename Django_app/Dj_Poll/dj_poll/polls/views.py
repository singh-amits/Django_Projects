from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {"question":question, "error_msg":"You did not select an option"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #Redirecting after successful vote so if the user hits back, vote doesn't count twice
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
