from django.urls import path
from account.views import UserCreateView,validate_phone,simple_message

urlpatterns = [
    path('home/',UserCreateView.as_view()),
    path('home/validate-phn', validate_phone),
    path('simple-message/', simple_message, name='simple-message'),
]

