from django.contrib import admin

# Register your models here.

from book.models import Book
from book.models import BookItem

admin.site.register(Book)
admin.site.register(BookItem)
