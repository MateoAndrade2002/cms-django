from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from registration.views import get_user_list
from frontend.views import edit_seo_home
from gallery.views import media_list, upload_media
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    return render(request, 
                    'account/dashboard.html',
                    {'section': 'dashboard'})

@login_required
def profile(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    profile = user.profile

    context = {'section': 'profile', 'profile': profile, 'viewed_user': user}

    return render(request, 'account/profile.html', context)

@login_required
def settings(request):
    seo_context = edit_seo_home(request)

    context = {
        'section': 'settings',
        'seo_edit_form': seo_context['seo_edit_form'],
    }
    
    return render(request, 'account/settings.html', context)


@login_required
def users(request):
    users_context = get_user_list(request)
    context = {
        'section': 'users',
        'users': users_context['users'],
    }

    return render(request, 'account/users.html', context)

@login_required
def gallery(request):
    gallery_context = media_list(request)
    form_media_context = upload_media(request)
    context = {
        'section': 'gallery',
        'gallery_content': gallery_context['media_files'],
        'form_media_context': form_media_context['form'],
    }

    return render(request, 'account/gallery.html', context)