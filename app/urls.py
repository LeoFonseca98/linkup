from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path
from posts.views import create_post_view, post_view
from account.views import healthz, register_view, login_view, logout_view, edit_profile_view, profile_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', lambda request: redirect('login')),
    path('healthz/', healthz, name='healthz'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('post_form/', create_post_view, name='post_form'),
    path('post/', post_view, name='post'),
    path('edit_profile/', edit_profile_view, name='profile_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

