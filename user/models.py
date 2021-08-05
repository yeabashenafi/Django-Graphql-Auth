from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField
# Create your models here.

class Extendeduser(AbstractUser):

    email = models.EmailField(blank=False,max_length=255,verbose_name="email")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"