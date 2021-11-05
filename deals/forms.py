from django import forms
from .models import Deal
from companies.models import Company
from contacts.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit

Field.template = 'custom_fields/custom_field.html'


class DealModelForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = (
            'deal_name',
            'contact_name',
            'company_name',
            'amount',
            'closing_date',
            'description',
        )
        help_texts = {
            'description': "This field will be visible in deals' list view."
        }

    def __init__(self, *args, **kwargs):
        super(DealModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-indigo-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'deal_name',
            'contact_name',
            'company_name',
            'amount',
            Field('closing_date', autocomplete='off'),
            'description',
            Submit('submit', 'Submit', css_class="flex px-6 py-2 ml-auto text-white bg-indigo-500 border-0 rounded focus:outline-none hover:bg-indigo-600")
        )
