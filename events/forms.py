from django import forms
from .models import Event
from contacts.models import Contact


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

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        contacts = Contact.objects.filter(user=request.user)
        super(EventModelForm, self).__init__(*args, **kwargs)
        self.fields['related_to'].queryset = contacts
