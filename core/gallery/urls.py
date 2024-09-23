from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path('', views.media_list, name="gallery")
]
