from django import forms
from .models import Event
from contacts.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

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
            'description': "This field will be visible in companies' list view."
        }

    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-pink-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'title',
            'date_from',
            'date_to',
            'repeat',
            'location',
            'related_to',
            'description',
            Submit('submit', 'Submit', css_class="flex px-6 py-2 ml-auto text-white bg-pink-500 border-0 rounded focus:outline-none hover:bg-pink-600")
        )