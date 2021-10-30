from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User

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
