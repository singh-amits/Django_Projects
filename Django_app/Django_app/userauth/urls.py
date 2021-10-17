import quiz
from django.urls import path, include
from . import views

app_name = "userauth"
urlpatterns = [
    path('', views.HomePageView.as_view(), name="homepage"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('otp/', views.OTPVerificationView.as_view(), name="otp"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),
    
]