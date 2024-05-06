from django import forms
from account.models import MyUser
class UserInfoForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = MyUser
