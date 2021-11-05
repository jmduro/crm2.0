from django import forms
from django.contrib.auth import get_user_model
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

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
            'featured',
        )
        help_texts = {
            'description': "This field will be visible in companies' list view."
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-red-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
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
            'featured',
            Submit('submit', 'Submit', css_class="flex px-6 py-2 ml-auto text-white bg-red-500 border-0 rounded focus:outline-none hover:bg-red-600")
        )
