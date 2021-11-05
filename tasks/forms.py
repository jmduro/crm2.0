from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'task_name',
            'due_date',
            'repeat',
            'related_to',
            'description',
            'priority',
        )
        help_texts = {
            'description': "This field will be visible in companies' list view."
        }

    def __init__(self, *args, **kwargs):
        super(TaskModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'block text-blue-700 text-sm font-bold mb-2'
        self.helper.layout = Layout(
            'task_name',
            'due_date',
            'repeat',
            'related_to',
            'description',
            'priority',
            Submit('submit', 'Submit', css_class="flex px-6 py-2 ml-auto text-white bg-blue-500 border-0 rounded focus:outline-none hover:bg-blue-600")
        )
