from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15)

    @property
    def full_name(self):
        return self.first_name+" "+self.last_name

    def __str__(self):
        return self.name
