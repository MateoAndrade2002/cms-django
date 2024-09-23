from django.shortcuts import render, redirect
from .models import MediaFile
from .forms import MediaFileForm
from .utils import check_media_directory
from django.contrib import messages

# Create your views here.

def media_list(request):
    check_media_directory()
    media_files = MediaFile.objects.all()
    return {'media_files': media_files}

def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Media uploaded!')
            form = MediaFileForm()
    else:
        form = MediaFileForm()
        
    return {'form':form}