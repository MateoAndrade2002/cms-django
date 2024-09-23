from django.contrib import admin
from .models import HomeSeo

# Register your models here.
@admin.register(HomeSeo)
class HomeSeoAdmin(admin.ModelAdmin):
    list_display = ['title']