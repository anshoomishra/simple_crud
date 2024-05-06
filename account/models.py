from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
# Create your models here.

class MyUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, default="", db_index=True)
