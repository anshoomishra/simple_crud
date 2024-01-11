from django.urls import path
from api.views import CreateBookApi
urlpatterns = [
    path('book/create/',CreateBookApi.as_view(),name="book-create"),
    path('book/update/<int:pk>/',CreateBookApi.as_view(),name="book-create"),

]