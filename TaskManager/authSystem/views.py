from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

# czy hasła sa takie same
# czy username wolny
# czy email wolny
# walidacja hasła


 
# Make a regular expression
# for validating an Email
 
# Define a function for
# for validating an Email
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html',{'form':RegisterForm()})
    else: #POST
        # pobieranie danych(login, email, hasło) z formularza w register.html
        # formularz zmodyfikowany w forms.py z UserCreationForm na RegisterForm zeby był email
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2: #sprawdzanie czy hasło sie powtarza
            # sprawdzanie czy login i email w bazie danych jest
            usernameTaken = User.objects.filter(username=username).exists()
            emailTaken = User.objects.filter(email=email).exists()
            if emailTaken:
                error = 'This email is already taken. Try again'
            if usernameTaken:
                error = 'This username is already taken. Try again'
            if not emailTaken and not usernameTaken:
                emailValid = check(email)
                if emailValid:
                    # walidacja hasła (sprawdzanie czy spełna odpowiednie kryteria)
                    # dodatkowo obsługa wyjątków w przypadku nie spełnienia warunków
                    try:
                        passwordValid = validate_password(password1)
                    except ValidationError as e:
                        passwordErrors = e.messages
                        return render(request, 'register.html',{'passwordErrors':passwordErrors,'form':RegisterForm()})
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password1)
                        return redirect('home')
                else:
                    error = 'Invalid email. Try again'
        else:
            error = 'Your password did not match. Try again'
        
        return render(request, 'register.html',{'message':error,'form':RegisterForm()})

def login_user(request):
    # sprawdzanie czy poprawne dane
    if request.method == 'GET':
        return render(request, 'login_user.html',{'form':AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            usernameExist = User.objects.filter(username=username).exists()
            if usernameExist:
                error = 'Password is not correct. Try again'
            else:
                error = f'Username {username} does not exist. Try again'
            return render(request, 'login_user.html',{'login_message':error,'form':AuthenticationForm()})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

