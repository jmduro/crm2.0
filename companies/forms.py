from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'company_name',
            'phone',
            'website',
            'description',
            'billing_street',
            'billing_city',
            'billing_state',
            'billing_country',
            'billing_code',
            'featured',
        )
        help_texts = {
            'description': "This field will be visible in companies' list view."
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-purple-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'company_name',
            'phone',
            'website',
            'description',
            'billing_street',
            'billing_city',
            'billing_state',
            'billing_country',
            'billing_code',
            'featured',
            Div(
                    Submit('submit', 'Submit', css_class="px-6 py-2 text-white bg-purple-500 border-0 rounded hover:bg-purple-600 text-center"), css_class='flex flex-col flex-wrap w-1/3 mx-auto mt-10'),
        )
