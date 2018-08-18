from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('upload/', views.upload, name="upload"),
    #path('profile/', views.profile, name="profile"),
    #path('albums/', views.albums, name="albums"),
]