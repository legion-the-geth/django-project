from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import User

def widget(request):
    if 'current_user' in request.session:
        c_u = request.session['current_user']
    else:
        c_u = None
    return render(request, 'accounts/widget.html', {'current_user': c_u})

def login(request):
    user = User.objects.get(login=request.POST['login'])
    if user.password == request.POST['password']:
        request.session['current_user'] = user
        return render(request, 'polls:index', {
            'err_login': "Wrong login credentials",
        })
    else:
        return HttpResponseRedirect(reverse('polls:index'))
