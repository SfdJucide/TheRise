from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='фото')
    age = models.PositiveIntegerField(null=True, verbose_name='возраст')
    experience = models.PositiveBigIntegerField(default=0, verbose_name='XP')

    def safe_delete(self):
        self.is_active = False
        self.save()


class UserProfile(models.Model):
    class Genders(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
    
    user = models.OneToOneField(User, null=False, unique=True, on_delete=models.CASCADE, db_index=True)
    gender = models.CharField(choices=Genders.choices, max_length=6, verbose_name='пол')
