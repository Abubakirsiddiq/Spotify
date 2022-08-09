from django.contrib import admin
from django.urls import path, include
from music.views import *
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="Spotify Api",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. Email:<xojiakbargoipov3@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


# router=DefaultRouter()
# router.register("qoshiqchilar", QoshiqchilarVS)
# router.register("albomlar", AlbomlarVS)
# router.register("qoshiqlar", AlbomlarVS)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('docs/',schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('qoshiqchilar/', QoshiqchilarListCreate.as_view()),
    path('qoshiqchi/<int:pk>/', Qoshiqchi.as_view()),
    path('albomlar/', AlbomlarListCreate.as_view()),
    path('albom/<int:pk>/', Albom.as_view()),
    # path('', include(router.urls)),
    # path('token-ber', TokenObtainPairView.as_view(), name='token_olish'),
    # path('token-yangila', TokenRefreshView.as_view(), name='token_yangilash'),
]

