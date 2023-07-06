from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(_("password"), max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


