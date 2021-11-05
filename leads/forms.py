from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'title',
            'email',
            'agent',
            'mobile',
            'phone_number',
            'home_phone',
            'description',
            'category'
        )

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model= User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'phone',
#             )
#         field_classes = {'username': UsernameField}


# class AssignAgentForm(forms.Form):
#     agent = forms.ModelChoiceField(queryset = Agent.objects.none())

#     def __init__(self, *args, **kwargs):
#         request = kwargs.pop('request')
#         print(request.user)
#         agents = Agent.objects.filter(organisation = request.user.userprofile)
#         super(AssignAgentForm, self).__init__(*args, **kwargs)
#         self.fields['agent'].queryset = agents

# class LeadCategoryUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Lead
#         fields = (
#             'category',
#         )