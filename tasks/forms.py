from django import forms
from .models import *


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

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        contacts = Contact.objects.filter(user=request.user)
        super(TaskModelForm, self).__init__(*args, **kwargs)
        self.fields['related_to'].queryset = contacts
