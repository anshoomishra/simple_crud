from django.shortcuts import render
from rest_framework import generics
from book.models import Book
from serializers.BookSerializer import BookSerializer
# Create your views here.

class CreateBookApi(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            data = serializer.save()
            print(data)
        return

class UpdateBookApi(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer