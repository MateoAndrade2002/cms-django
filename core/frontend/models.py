from django.db import models

# Create your models here.
class HomeSeo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    robots = models.CharField(max_length=255, blank=True, null=True)
    og_title = models.CharField(max_length=70, blank=True, null=True)
    og_description = models.CharField(max_length=160, blank=True, null=True)
    og_image_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'SEO Home'
        verbose_name_plural = "SEO Home"

    def __str__(self):
        return self.title