from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, ProfileView, WaitActivationView, EmailVerificationView, UserPasswordResetView

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/whait', WaitActivationView.as_view(), name='wait_activation'),
    path('verify-email/', EmailVerificationView.as_view(), name='verify_email'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile')
]