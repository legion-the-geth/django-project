from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import exceptions
from accounts.models import User

def widget(request):
    if 'current_user' in request.session:
        c_u = request.session['current_user']
    else:
        c_u = None
    return render(request, 'accounts/widget.html', {'current_user': c_u})

def login(request):
    try:
        user = User.objects.get(
            login=request.POST['login'],
            password=request.POST['password'],
        )
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('polls:index') + "?wrong_login")
    else:
        request.session['current_user'] = user
        return HttpResponseRedirect(reverse('polls:index'))
