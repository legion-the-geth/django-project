from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
# from accounts import views

from accounts.models import User
from .models import Question, Choice

def index(request):
    questions = Question.get_last_x_questions(5)
    current_user = User.get_current(request.session)

    return render(request, 'polls/index.html', {'lql':questions, 'current_user':current_user,})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # Excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        # Excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())

class CreateView(generic.CreateView):
    model = Question
    fields = ('question_text',)
    success_url = '../'

    def form_valid(self, form):
        current_user = User.get_current(self.request.session)
        form.instance.publisher = current_user
        return super(CreateView, self).form_valid(form)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    # question = Question.objects.filter(pub_date__lte=timezone.now(), pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
