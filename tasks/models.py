from django.db import models
from users.models import User
from contacts.models import Contact

# Create your models here.

class Task(models.Model):

    REPEAT = True
    DONT_REPEAT = False
    REPEAT_CHOICES = [
        (REPEAT, 'Repetir'),
        (DONT_REPEAT, 'No repetir'),
    ]

    PRIORITY_VERY_HIGH = 'Muy alta'
    PRIORITY_HIGH = 'Alta'
    PRIORITY_MEDIUM = 'Media'
    PRIORITY_LOW = 'Baja'
    PRIORITY_VERY_LOW = 'Muy baja'
    PRIORITY_CHOICES = [
        (PRIORITY_VERY_HIGH, 'Muy alta'),
        (PRIORITY_HIGH, 'Alta'),
        (PRIORITY_MEDIUM, 'Media'),
        (PRIORITY_LOW, 'Baja'),
        (PRIORITY_VERY_LOW, 'Muy baja')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    due_date = models.DateField()
    repeat = models.BooleanField(default=DONT_REPEAT, choices=REPEAT_CHOICES)
    related_to = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)

    def __str__(self):
        return f'{self.task_name}'
