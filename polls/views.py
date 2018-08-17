from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lql': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # # Avec Try catch : 
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # # Raccourci :
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':q})

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))