from django.db import models
from account.models import MyUser
# Create your models here.


class BookItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issued_to = models.ForeignKey(MyUser,on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    isbn = models.CharField(max_length=100,blank=True)
    writer = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title
