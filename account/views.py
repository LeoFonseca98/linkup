from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, ProfileForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home_view(request): 
    return render(request, "home.html")


def healthz(request):
    return render(request, "OK", 200)


def register_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            print(user_form)
            return redirect('login')
        else:
            user_form = CustomUserCreationForm()
    else: 
        user_form = CustomUserCreationForm()
    return render(request, "register.html", {'user_form': user_form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post')
            else:
                login_form = AuthenticationForm()


        except User.DoesNotExist:
            login_form = AuthenticationForm()
            return render(request, 'login.html', {
                'login_form': login_form,
                'error': 'Email não encontrado.'})     
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



login_required
def logout_view(request):
    logout(request)
    return redirect('login')


