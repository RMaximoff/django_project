from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Email', unique=True)

    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone number', **NULLABLE)
    country = models.CharField(max_length=235, verbose_name='Country', **NULLABLE)
    email_verification_token = models.CharField(max_length=235, verbose_name='Токен верификации')
    is_verified = models.BooleanField(default=False, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
