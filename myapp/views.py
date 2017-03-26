from django.http import HttpResponseRedirect
from myapp.models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

"""def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'myapp/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'question': question})"""

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myapp/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, id = question_id)
    try:
        selected_choice = p.choice_set.get(id = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'myapp/detail.html', {
            'question':p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results', args=(p.id,)))
