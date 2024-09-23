import os
from django.conf import settings
from .models import MediaFile

def check_media_directory():
    media_directory = settings.MEDIA_ROOT
    existing_media_files = set(MediaFile.objects.values_list('image', flat=True))

    for root, dirs, files in os.walk(media_directory):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, settings.MEDIA_ROOT)

                if relative_path not in existing_media_files:
                    title = os.path.splitext(file)[0]
                    MediaFile.objects.create(image=relative_path, title=title)

    # Eliminar archivos físicos que ya no tienen una entrada en MediaFile
    for media_file in MediaFile.objects.all():
        if not os.path.exists(os.path.join(media_directory, media_file.image.name)):
            media_file.delete()