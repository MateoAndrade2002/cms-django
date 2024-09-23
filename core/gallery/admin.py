from django.contrib import admin
from .models import MediaFile

# Register your models here.
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_url']
    readonly_fields = ['image_url']