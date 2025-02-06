from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Song, Book,User
from .forms import RegisterForm,LoginForm 
from django.db.models import Q

def home(request):
    latest_songs = Song.objects.all()[:6]  # Get 6 latest songs
    latest_books = Book.objects.all()[:4]  # Get 4 latest books
    return render(request, 'home.html', {
        'latest_songs': latest_songs,
        'latest_books': latest_books
    })
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if confirm_password == password:
                User.objects.create(username=username, email=email, phone_number=phone_number,password=make_password(password))
                return redirect('login')
        else:
            print("invalid",form.errors)
    return render(request, 'user/register.html',{'form':form})


def login_auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_email = form.cleaned_data['username']
            print("username",username_email)
            password = form.cleaned_data['password']
            user = User.objects.get(Q(username=username_email)| Q(email=username_email))
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials, please try again.')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


