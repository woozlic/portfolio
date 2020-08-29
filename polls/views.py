from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def show_polls(request):
    polls = get_list_or_404(Question)
    content = {'polls':polls}
    return render(request, "polls/index.html", content)
def detail_poll(request, pk):
    poll = get_object_or_404(Question, pk=pk)
    content = {'poll':poll}
    return render(request, "polls/detail.html", content)
def vote(request, pk):
    question = get_object_or_404(Question,pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        content = {'question':question, 'error_message':'You didn\'t select a choice'}
        return render(request, 'polls/detail.html', content)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(pk,)))

    #return render(request, "polls/vote.html", content)
def results(request,pk):
    content = {}
    return render(request, "polls/results.html", content)