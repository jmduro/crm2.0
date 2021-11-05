from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'phone'
                  )
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'Username'}
        self.fields['email'].widget.attrs = {'placeholder': 'example@mail.com'}
        self.fields['first_name'].widget.attrs = {'placeholder': 'First name'}
        self.fields['last_name'].widget.attrs = {'placeholder': 'Last name'}
        self.fields['phone'].widget.attrs = {'placeholder': 'Phone number'}
        self.helper = FormHelper()
        self.helper.label_class = 'block text-red-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
                'username',
                'email',
                'first_name',
                'last_name',
                'phone',
            Submit('submit', 'Submit', css_class="flex px-6 py-2 ml-auto text-white bg-red-500 border-0 rounded focus:outline-none hover:bg-red-600")
        )