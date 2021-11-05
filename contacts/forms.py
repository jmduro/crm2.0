from django import forms
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'title',
            'email',
            'company_name',
            'mobile',
            'phone',
            'home_phone',
            'email_opt_out',
            'description',
        )