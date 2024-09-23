from django.urls import path
from . import views
from registration.views import edit
from django.contrib.auth import views as auth_views
# from frontend.views import edit_seo_home

app_name = "account"

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('users/', views.users, name='users'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/edit/<str:username>/', edit, name='edit'),
    path('gallery/', views.gallery, name='gallery')
]
