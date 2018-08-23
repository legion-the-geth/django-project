from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import exceptions
from accounts.models import User

def widget(request):
    return render(request, 'accounts/widget.html')

def login(request):
    try:
        user = User.objects.get(
            login=request.POST['login'],
            password=request.POST['password'],
        )
    except User.DoesNotExist:
        request.session['current_user_id'] = 0
        return HttpResponseRedirect(reverse('polls:index') + "?wrong_login=1")
    else:
        request.session['current_user_id'] = user.id
        return HttpResponseRedirect(reverse('polls:index'))

def logout(request):
    del request.session['current_user_id']
    return HttpResponseRedirect(reverse('polls:index'))
