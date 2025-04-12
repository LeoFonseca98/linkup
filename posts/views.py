from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
from .models import Post


@login_required
def create_post_view(request):
    if request.method == "POST":
        post_form = PostModelForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('post')
    else:
        post_form = PostModelForm()
    return render(request, 'post_form.html', {'post_form': post_form})

@login_required
def post_view(request):
    posts = Post.objects.filter(usuario=request.user)
    return render(request, 'post.html', {'posts': posts})

def delete_post_view(request):
    post = Post.objects.filter(usuario=request.user)
    