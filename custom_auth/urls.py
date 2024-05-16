from django.urls import path
from .views import RegisterView, LoginView, UserProfileDetailView, UserProfileUpdateView, UserProfileDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import timedelta

class CustomTokenObtainPairView(TokenObtainPairView):
    token_refresh_lifetime = timedelta(days=7) 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:id>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserProfileDeleteView.as_view(), name='profile-delete'),
]
