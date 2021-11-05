from django.db import models
from contacts.models import Contact
from tasks.models import Task
from users.models import User

# Create your models here.

class Event(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    repeat = models.BooleanField(
        default=Task.DONT_REPEAT, choices=Task.REPEAT_CHOICES)
    location = models.CharField(max_length=50, blank=True)
    related_to = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.title}'