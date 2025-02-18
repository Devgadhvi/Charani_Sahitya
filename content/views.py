from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.contrib import messages
from .models import Song, Book,User,Feed_post
from .forms import RegisterForm,LoginForm ,FeedPostForm,ProfileEditForm
from django.db.models import Q

def home(request):
    latest_songs = Song.objects.all()[:6]  
    latest_books = Book.objects.all()[:4]  
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

def user_logout(request):
    logout(request) 
    return redirect('home')

def profile(request):
    profile = request.user.profile 
    user_posts = Feed_post.objects.filter(profile=profile) 

    return render(request, 'user/profile.html', {'profile': profile, 'feed': user_posts})

def ask_permissons(request,id):
    user = get_object_or_404(User, id=id)
    send_mail(
    f"{user.username} wants to be creator",
    ("""click on the link to give permisson "http://127.0.0.1:8000/be_a_creator" """),
    "jaydeeptalaviya7@gmail.com",
    ["devgadhavi951@gmail.com"],
    fail_silently=False,
)
    return redirect('home')

def feedpage(request):
    feed = Feed_post.objects.all()
    return render(request, 'feed/feedpage.html', {'feed': feed})

def creator_form(request):
    post = FeedPostForm()
    user = request.user
    if request.method == 'POST':
        post = FeedPostForm(request.POST)
        if post.is_valid():
            post_new =  post.save(commit=False)
            post_new.profile_id = user.profile.id
            post_new.save()
            return redirect('create')
    return render(request, 'feed/creator_form.html',{'post':post})

def post_detail(request, post_id):
    post = get_object_or_404(Feed_post, id=post_id)
    return render(request, 'feed/post_detail.html', {'post': post})


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the form data to user model
            form.save()

            # If profile picture is updated, save it
            if 'profile_picture' in request.FILES:
                user.profile.profile_picture = request.FILES['profile_picture']
                user.profile.save()

            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')  # Redirect to the profile page

    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'user/edit_profile.html', {'form': form})

