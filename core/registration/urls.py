from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "registration"

urlpatterns = [
    # Previous
    # path('login/', views.user_login, name='login'),

    # Login / Logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),
]
