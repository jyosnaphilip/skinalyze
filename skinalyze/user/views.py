from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render (request, 'users/index.html')

def features(request):
    return render (request, 'users/features.html')

def about(request):
    return render (request, 'users/about.html')

def review(request):
    return render (request, 'users/review.html')

def home(request):
    return render (request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Already Exists!")
                return redirect('user_login')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
                return redirect('user_login')

            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password1) #setting the password in hashed secured format.
                user.save()
                # automatically create a row in customUser table- profile pic  & gamemode can be changed
               
                # activationEmail(request, user, email)
                messages.success(request, 'Account Created Successfully ')
                return redirect('user_login')

        else:
            return redirect('user_login')
    else:
        return render(request, 'login/login.html')

def user_login(request): 
 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None: #authentication is successful
            login(request, user) #creates a session for the user when the user is logged in.
            
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('login')

    else:
        
        return render(request, 'login/login.html')
    


def winter_deep(request):
    return render(request, 'users/winter_deep.html')

def winter_cool(request):
    return render(request, 'users/winter_cool.html')

def winter_bright(request):
    return render(request, 'users/winter_bright.html')

def summer_soft(request):
    return render(request, 'users/summer_soft.html')

def summer_cool(request):
    return render(request, 'users/summer_cool.html')

def summer_light(request):
    return render(request, 'users/summer_light.html')

def spring_warm(request):
    return render(request, 'users/spring_warm.html')

def spring_light(request):
    return render(request, 'users/spring_light.html')

def spring_bright(request):
    return render(request, 'users/spring_bright.html')

def autumn_deep(request):
    return render(request, 'users/autumn_deep.html')

def autumn_warm(request):
    return render(request, 'users/autumn_warm.html')

def autumn_soft(request):
    return render(request, 'users/autumn_soft.html')
