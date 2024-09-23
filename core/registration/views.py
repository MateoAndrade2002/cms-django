from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})

def get_user_list(request):
    users_context = User.objects.all()
    context = {
        'users': users_context
    }
    return context

@login_required
def edit(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        profile_form = ProfileEditForm(instance=user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '¡Los datos se actualizaron correctamente!')
            return redirect('account:users')
        else:
            messages.error(request, 'Error updating the profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'edit_user': user})

def view_user(request, username=None):
    user = User.objects.get(username=username)
    return {'user': user}
