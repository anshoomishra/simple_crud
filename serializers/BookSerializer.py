from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self,value):
        print(value)
        if len(value)==0 :
            raise ValidationError(f"{value} can not be empty")
        return value

