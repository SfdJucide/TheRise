from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='фото')
    age = models.PositiveIntegerField(null=True, verbose_name='возраст')


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, unique=True, on_delete=models.CASCADE, db_index=True)
    