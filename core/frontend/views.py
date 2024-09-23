from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeSeoEditForm
from django.contrib import messages
from .models import HomeSeo


def get_seo_home(request):
    seo_instance = get_object_or_404(HomeSeo, pk=1)
    context = {'seo_instance': seo_instance}
    return render(request, 'frontend/frontend_base.html', context)

def edit_seo_home(request):
    seo_instance = get_object_or_404(HomeSeo, pk=1)
    
    if request.method == 'POST':
        seo_edit_form = HomeSeoEditForm(instance=seo_instance, data=request.POST)
        if seo_edit_form.is_valid():
            seo_edit_form.save()
            messages.success(request, '¡Los datos se actualizaron correctamente!')
    else:
        seo_edit_form = HomeSeoEditForm(instance=seo_instance)
    
    return {'seo_edit_form': seo_edit_form}