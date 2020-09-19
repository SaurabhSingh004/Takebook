from django.http import HttpResponse
from django.shortcuts import redirect, render

import os

from register.models import user

def profile(request):
    try:
        m = request.session['username']
        p = user.objects.get(mUsername = m)
        name = p.mName
        username = p.mUsername
        email = p.mEmail
        image = p.mImage
        context = {
            'name': name,
            'username': username,
            'email': email,
            'profilePic': image,
            'value': 'readonly',
            'allow': True,
            'in': 'none',
            'out': 'block',
            'valname':'Change',
            'visVal': 'hidden',
        }
        if 'Save' == request.POST.get('submit'):
            context['value'] = 'readonly'
            context['valname'] = 'Change'
            p = user.objects.get(mUsername = m)
            if request.POST.get('name').strip() != '':
                p.mName = request.POST.get('name')
                p.save()
                context['name'] = p.mName
            if request.POST.get('email').strip() != '':
                p.mEmail = request.POST.get('email')
                p.save()
                context['email'] = p.mEmail 
            
            # image upload implementation....
            if request.POST.get('avatar') is None:
                img = request.FILES['avatar']
                print(img)
                img_extension = os.path.splitext(img.name)[1]
                user_folder = 'register/static/register/' + str(m)
                
                if not os.path.exists(user_folder):
                    os.makedirs(user_folder)
                
                img_save_path = "%s/%s%s"%( user_folder, 'avatar', img_extension)
                
                with open(img_save_path, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)
                # Completed....
                p.mImage = img_save_path[9:]
                p.save()
                context['profilePic'] = p.mImage

        elif request.POST.get('submit'):
            context['value'] = ''
            context['valname'] = 'Save'
            context['visVal'] = 'visible'
        return render(request, 'Profile/profile.html', context)
    except:
        return redirect('/')

def userProfile(request, profilename):
    try:
        m = request.session['username']
        p = user.objects.get(mUsername = profilename.upper())
        name = p.mName
        username = p.mUsername
        email = p.mEmail
        image = "../../"+p.mImage
        context = {
            'name': name,
            'username': username,
            'email': email,
            'profilePic': image,
            'value': 'readonly',
            'allow': True,
            'in': 'none',
            'out': 'block',
            'valname':'Change',
            'visVal': 'hidden',
        }        
        if m == profilename.upper():
            return redirect('/profile')
        else:
            context['out'] = 'none'
            return render(request, 'Profile/profile.html', context)
    except:
        return redirect('/')
    