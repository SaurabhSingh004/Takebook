from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import user

def login(request):

    try:
        request.session['username']
        return redirect('/')
    except:
        context = {'visval': 'none'}
        if request.method == 'POST':
            username = request.POST.get('username').upper()
            password = request.POST.get('password')

            # Checking username and password....
            try:
                a = user.objects.get(mUsername = username)
                if(a.mPassword == password):
                    request.session['username'] = username
                    return redirect('/')
                else:
                    context['visval'] = 'block'
                    return render(request, 'login.html', context)
            except:
                context['visval'] = 'block'
                return render(request, 'login.html', context)
    return render(request, 'login.html', context)

def signup(request):
    
    try:
        request.session['username']
        return redirect('/')
    except:    
        if request.method == 'POST':
            name = request.POST.get('name').upper()
            email = request.POST.get('email').upper()
            username = request.POST.get('username').upper()
            password = request.POST.get('password')

            # Saving new user's to database....
            p = user.objects.create(mName = name, mEmail = email, mUsername = username, mPassword = password) 
            p.save()
            return redirect('/login/')

    return render(request, 'signup.html')