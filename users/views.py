import string
import random

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:wait_activation')

    def send_email(self, user, token):
        send_mail(
            'Подтверждение регистрации',
            f'{self.request.build_absolute_uri(reverse("users:verify_email"))}?token={token}',
            settings.EMAIL_HOST_USER,
            [user.email]
        )

    def form_valid(self, form):
        user = form.save(commit=False)
        token = default_token_generator.make_token(user)
        user.email_verification_token = token
        self.send_email(user, token)
        user.save()
        return super().form_valid(form)


class EmailVerificationView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        user = get_object_or_404(User, email_verification_token=token)
        user.is_verified = True
        user.save()
        return redirect('users:login')
# asdad__dasdrf334


class WaitActivationView(TemplateView):
    template_name = 'users/activation.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(View):
    def send_password(self, user, password):
        send_mail(
            'Новый пароль',
            f'{password}',
            settings.EMAIL_HOST_USER,
            [user.email]
        )

    def get(self, request, *args, **kwargs):
        user = self.request.user
        print(user._meta)
        if user.is_authenticated:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            print(user._meta)
            self.send_password(user, password)
            print(user._meta)
            user.set_password(password)
            print(user._meta)
            user.save()
        return redirect('users:login')
