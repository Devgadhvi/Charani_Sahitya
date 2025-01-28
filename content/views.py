from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.hashers import make_password
from .models import Song, Book,User
from .forms import RegisterForm

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
        form = RegisterForm(request.POST)  # Corrected request.POST
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            # Create the user and hash the password
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('login') 
    return render(request, 'user/register.html', {'form': form})

def login(request):
    return render(request, 'user/login.html')
        
