from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import friends
from register.models import user

def home(request):
    try:
        username = request.session['username']
        context = {'username': username}
    
        p = friends.objects.filter(mUsername = username)
        context['friend'] = p
    
        return render(request, 'home.html', context)
    except:
        return redirect('/login/')


def logout(request):
    try:
        request.session['username']
        del request.session['username']
    finally:
        return redirect('/')