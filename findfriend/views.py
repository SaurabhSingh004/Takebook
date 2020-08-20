from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.decorators.clickjacking import xframe_options_sameorigin

from register.models import user
from home.models import friends
from .models import Request

def find(request):
    try:
        username = request.session['username']
        context = {}
        friend = [username]

        users = user.objects.all()
        frnd = friends.objects.filter(mUsername = username)
        for i in frnd:
            friend.append(i.mFriendUser.mUsername)
        
        # checking requests sent or received....
        sent_request = Request.objects.filter(mSent= username)
        for i in sent_request:
            friend.append(i.mReceived.mUsername)
        
        received_request = Request.objects.filter(mReceived = username)
        for i in received_request:
            friend.append(i.mSent.mUsername)

        context['users'] = users
        context['friend'] = friend

        return render(request, 'findfriend/find.html', context)
    except:
        return redirect('/login/')  


def sentReq(request, friendname):
    try:
        username = request.session['username']
        # creating request to the user....
        userobj = user.objects.get(mUsername=username)
        friendobj = user.objects.get(mUsername=friendname)
        create = Request.objects.create(mSent = userobj, mReceived = friendobj)
        create.save()
        return redirect('/home/find/')
    except:
        return HttpResponse("wrong")

@xframe_options_sameorigin
def receivedReq(request):
    try:
        username = request.session['username']
        context = {}
        show_request = Request.objects.filter(mReceived=username)
        context['Requests'] = show_request
        return render(request, 'findfriend/received.html', context)
    except:
        return HttpResponse("You're always wrong")

def process(request, action, friendname):
    try:
        username = request.session['username']
        userobj = user.objects.get(mUsername=username)
        friendobj = user.objects.get(mUsername=friendname)
        # adding friend and deleting request....
        if action == 'add':
            addfriend = friends.objects.create(mUsername=userobj, mFriendUser=friendobj)
            alteraddfriend = friends.objects.create(mFriendUser=userobj, mUsername=friendobj)
            addfriend.save()
            alteraddfriend.save()
            del_request = Request.objects.filter(mReceived=username, mSent=friendname)
            del_request.delete()

        elif action == 'del':
            del_request = Request.objects.filter(mReceived=username, mSent=friendname)
            del_request.delete()

        return redirect('/home/received/')

    except:
        return HttpResponse("u again here")
