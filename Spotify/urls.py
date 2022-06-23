from django.contrib import admin
from django.urls import path
from music.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloAPI.as_view(), name="hello"),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view(), name="qoshiqchilar"),
    path('qoshiqchi/<int:pk>/', QoshiqchiAPIView.as_view(), name="qoshiqchi"),
    path('albomlar/', AlbomlarAPIView.as_view(), name="albomlar"),
    path('albom/<int:pk>/', AlbomAPIView.as_view(), name="albom"),
    path('qoshiqlar/', QoshiqlarAPIView.as_view(), name="qoshiqlar"),
]

