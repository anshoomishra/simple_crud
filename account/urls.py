from django.urls import path
from account.views import UserCreateView,validate_phone

urlpatterns = [
    path('home/',UserCreateView.as_view()),
    path('home/validate-phn', validate_phone)
]

