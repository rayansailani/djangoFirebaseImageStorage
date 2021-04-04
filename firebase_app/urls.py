from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.firebase_view, name="firebase_view"),
    path('images', views.images_view, name="images"),
]
