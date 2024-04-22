"""
URL configuration for movie_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import MovieListCreate, MovieRetrieveUpdateDestroy
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="Movie Service API",
      default_version='v1',
      description="API to manage a list of movies",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@movie-service.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    # Ajout et Récupération des movies
    path('api/movies/', MovieListCreate.as_view(), name='movie-list-create'),
    # Suppression , GetById et modification des movies
    path('api/movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
]