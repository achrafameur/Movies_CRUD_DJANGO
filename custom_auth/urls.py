from django.urls import path
from .views import RegisterView, LoginView, UserProfileDetailView, UserProfileUpdateView, UserProfileDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:id>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserProfileDeleteView.as_view(), name='profile-delete'),
]
