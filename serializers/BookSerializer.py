from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from book.models import Book
import logging
logger = logging.getLogger(__name__)

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self,value):
        logger.debug(f'Title value: {value}')
        if not value.strip():
            raise ValidationError(f"{value} can not be empty")
        return value

    def validate_description(self,value):
        print(self)
        if not value.strip():
            raise ValidationError(f"{value} can not be empty")
        return value

