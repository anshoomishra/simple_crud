from account.models import MyUser
from rest_framework import serializers
from book.models import Book

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username','name','phone_number','email']



