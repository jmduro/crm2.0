from django import forms
from django.contrib.auth import get_user_model
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

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
            'description': "This field will be visible in contacts' list view."
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
            Div(
                    Submit('submit', 'Submit', css_class="px-6 py-2 text-white bg-red-500 border-0 rounded hover:bg-red-600 text-center"), css_class='flex flex-col flex-wrap w-1/3 mx-auto mt-10'),
        )
