from django import forms
from .models import *


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
