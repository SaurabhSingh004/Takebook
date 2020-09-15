from django.http import HttpResponse
from django.shortcuts import redirect, render
from json import dumps 
import os
import json

from .models import friends, Posts
from register.models import user

def home(request):
    try:
        username = request.session['username']
        context = {'username': username}
        friendlist = friends.objects.filter(mUsername = username)
        # return HttpResponse(friendlist)
        arrPost = []
        for i in friendlist:
            k = Posts.objects.filter(mUser = i.mFriendUser.mUsername)
            for x in k:
                val = {"photo": x.mPhoto, "caption":x.mCaption, "username":x.mUser.mUsername, "userphoto":x.mUser.mImage}
                arrPost.append(val)    
        p = Posts.objects.filter(mUser = username)
        for i in p:
            val = {"photo": i.mPhoto, "caption":i.mCaption, "username":i.mUser.mUsername, "userphoto":i.mUser.mImage}
            arrPost.append(val)

        newarr = json.dumps(arrPost)
        context['postcontext'] = p
        context['jsoncontext'] = newarr


        if request.method == 'POST':
            userobj = user.objects.get(mUsername= username)
            caption = request.POST.get('caption')
            if(caption.strip() == ''):
                caption = 'Image by: '+username
            img = request.FILES['imageUpload']
            user_folder = 'register/static/register/' + str(username)+'/posts'
            
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)
                
            img_save_path = "%s/%s"%( user_folder, img)
            with open(img_save_path, 'wb+') as f:
                for chunk in img.chunks():
                    f.write(chunk)
            photo = img_save_path[9:]
            p = Posts.objects.create(mUser=userobj,mPhoto=photo, mCaption=caption)
            p.save()
    
        return render(request, 'home.html', context)
    except:
        return redirect('/login/')


def logout(request):
    try:
        request.session['username']
        del request.session['username']
    finally:
        return redirect('/')