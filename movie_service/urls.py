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
from .views import MovieDetail, MovieList, CategoryCreate, MovieCategories, CategoryMovies, MovieSearch
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

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
    path('openapi-schema/', schema_view.without_ui(cache_timeout=0), name='openapi-schema'),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    path('admin/', admin.site.urls),
    # # Ajout et Récupération des movies
    # path('api/movies/', MovieListCreate.as_view(), name='movie-list-create'),
    # # Suppression , GetById et modification des movies
    # path('api/movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
    path('api/movies/', MovieList.as_view(), name='movie-list'),
    path('api/movies/create/', MovieList.as_view(), name='movie-create'),
    path('api/movies/detail/', MovieDetail.as_view(), name='movie-detail'),
    path('api/movies/update/', MovieDetail.as_view(), name='movie-update'),
    path('api/movies/delete/', MovieDetail.as_view(), name='movie-delete'),
    path('api/movies/search/', MovieSearch.as_view(), name='movie-search'),
    path('api/categories/', CategoryCreate.as_view(), name='category-create'),
    path('api/movies/<int:pk>/categories/', MovieCategories.as_view(), name='movie-categories'),
    path('api/categories/<int:pk>/movies/', CategoryMovies.as_view(), name='category-movies'),
]