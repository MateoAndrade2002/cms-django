from django import forms
from .models import HomeSeo

class HomeSeoEditForm(forms.ModelForm):
    class Meta:
        model = HomeSeo
        fields = '__all__'