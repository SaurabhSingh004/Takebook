from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.decorators.clickjacking import xframe_options_sameorigin

from home.models import friends
from register.models import user
from .models import Chat

def chat(request):
    
    context = {}
    try:
        username = request.session['username']
        p = friends.objects.filter(mUsername = username)
        context['friend'] = p
        return render(request, "chathome/chatarea.html", context)
    except:
        return redirect('/login/')

@xframe_options_sameorigin
def chatarea(request, friend):
    
    try:
        username = request.session['username']
        fromVal = user.objects.get(mUsername = username)
        toVal = user.objects.get(mUsername = friend)
        context = {}
        context['currentfrnd'] = friend

        if request.method == "POST":
            # Storing messages in user and away user's db....
            message = request.POST.get('message')
            print("msg is  ", message)
            userfield = Chat.objects.create(mFrom = fromVal, mTo = toVal, mSent = message)
            friendfield = Chat.objects.create(mFrom = toVal, mTo = fromVal, mReceived = message)
            userfield.save()
            friendfield.save()

        # To fetch chats.... 
        msg = Chat.objects.filter(mFrom=username, mTo=friend)
        context['msg'] = msg
        
        return render(request, 'chatarea/chat.html', context)

    except:
        return HttpResponse("bye")