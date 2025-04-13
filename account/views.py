
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        else:
            user_form = UserCreationForm()
    else: 
        user_form = UserCreationForm()
    return render(request, "register.html", {'user_form': user_form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post')
        else: 
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def profile_view(request):
    profile = Profile.objects.get_or_create(user=request.user)
    print(profile)
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = ProfileForm()

    if request.method == "POST":
        profile = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile.is_valid():
            profile.save()
            return redirect('profile')
    else:
        profile = ProfileForm()
        return render(request, 'edit_profile.html', {'profile': profile})






def logout_view(request):
    logout(request)
    return redirect('home')

