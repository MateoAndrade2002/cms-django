from django.db import models
import os

# Create your models here.
class MediaFile(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}, {self.title}"
    
    def delete(self, *args, **kwargs):
        # Eliminar archivo físico solo si se elimina explícitamente desde el admin
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    def image_url(self):
        if self.image:
            return self.image.url
        
    image_url.short_description = 'Image URL'