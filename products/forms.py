from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_name',
            'product_code',
            'product_category',
            'unit_price',
            'description',
            'product_active',
            )
        help_texts = {
            'description': "This field will be visible in companies' list view."
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-green-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'product_name',
            'product_code',
            'product_category',
            'unit_price',
            'description',
            'product_active',
            Div(
                Submit('submit', 'Submit', css_class="px-6 py-2 text-white bg-green-500 border-0 rounded hover:bg-green-600 text-center"), css_class='flex flex-col flex-wrap w-1/3 mx-auto mt-10'),
        )
