from os import stat_result
from face_recog.views import capture_and_store
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
# Create your views here.

Password = 'User@123' #COmmon password for all users

# Super User
# Uername - OnlineVault
# password - Vault123

def login_signup(request):
    if request.user.is_authenticated:
        return redirect('captureandstore',status=1)
    return render(request, 'authentication/authenticate.html')

def authentication(request):
    
    if request.method == 'POST':        
        email = request.POST['user_email']        
        user = User.objects.filter(email=email).first()  
        request.session['user_mail'] = email
        
        if user is not None:
            request.session['user_id'] = user.id
            #login(request,user)
            return redirect('captureandstore',status=1)
            return redirect('webcam',status=1)
            
        else:
            username = email.split('@')[0]
            user = User(username=username, password=Password,email=email)
            user.save()
            request.session['user_id'] = user.id
            #login(request,user)
            return redirect('captureandstore',status=2)
            return redirect('webcam',status=2)
            
    return HttpResponse('Uhh oHH something wrong :(')
    

def user_logout(request):
    logout(request)
    return redirect('login_signup')
    
def page_not_found(request):
    return render(request,'authentication/page_not_found.html')