from django.urls import path
from . import views

urlpatterns = [
    path('api/auth/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('api/auth/login/', views.UserLoginView.as_view(), name='user-login'),
  
]