from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import HomeSeoEditForm
from .models import HomeSeo

def handle_seo_post(request):
    seo_instance = get_object_or_404(HomeSeo, pk=1)
    seo_edit_form = HomeSeoEditForm(instance=seo_instance, data=request.POST)
    if seo_edit_form.is_valid():
        seo_edit_form.save()
        messages.success(request, 'Datos actualizados correctamente')
    return {
        'seo_instance': seo_instance,
        'seo_edit_form': seo_edit_form,
    }