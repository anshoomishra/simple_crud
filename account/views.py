from django.shortcuts import render
from django.views.generic import CreateView
from account.forms import UserInfoForm
from django.shortcuts import render
import phonenumbers

# Create your views here.

class UserCreateView(CreateView):
    template_name = 'account/home.html'
    success_url = '/'
    form_class = UserInfoForm


def validate_phone(request):
    if request.method == 'POST':
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')

        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            if is_valid:
                message = f"The phone number {phone_number} is valid."
            else:
                message = f"The phone number {phone_number} is not valid for the selected country code {country_code}."
        except phonenumbers.phonenumberutil.NumberParseException:
            message = "Invalid phone number format."

        return render(request, 'account/results.html', {'message': message})

    return render(request, 'account/home.html')