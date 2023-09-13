from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

# # Create your views here.

def user_signup(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        username = request.POST['username']
        user_pswd = request.POST['user_pass']

        print('user_pswd: ', user_pswd)
        print('username: ', username)
        print('user_email: ', user_email)
        user_model = get_user_model()
        
        if not username.strip():
            messages.error(request, 'Something is wrong.')
            return render(request, 'signup.html')
        
        if user_model.objects.filter(email=user_email).exists():

            messages.error(request, 'Something is wrong.')
            return render(request, 'signup.html') 
        
        user_obj = user_model.objects.create_user(email=user_email, password = user_pswd, username=username)
        user_obj.set_password(user_pswd)
        user_obj.save()
        user_auth = authenticate(username = username, password=user_pswd)
        print('user_auth: ', user_auth)
        if user_auth:
            login(request, user_auth) 
            return render(request,'home.html')
    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        user_pswd = request.POST['user_pass']
        try:
            user_auth = authenticate(username=user_email, password=user_pswd)
            print('user_auth: ', user_auth)
            login(request, user_auth)
            return render(request, 'home.html')
        except:
            messages.error(request, 'Something is wrong.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
        
    
def user_logout(request):
    try:
        logout(request)
    except:
        messages.error(request, 'Something is wrong.')
    return redirect('login')
