from django import forms
from .models import Event
from contacts.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Div

Field.template = 'custom_fields/custom_field.html'

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'title',
            'date_from',
            'date_to',
            'repeat',
            'location',
            'related_to',
            'description',
        )
        help_texts = {
            'description': "This field will be visible in events' list view."
        }

    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-pink-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'title',
            Field('date_from', autocomplete='off'),
            Field('date_to', autocomplete='off'),
            'repeat',
            'location',
            'related_to',
            'description',
            Div(
                    Submit('submit', 'Submit', css_class="px-6 py-2 text-white bg-pink-500 border-0 rounded hover:bg-pink-600 text-center"), css_class='flex flex-col flex-wrap w-1/3 mx-auto mt-10'),
        )
