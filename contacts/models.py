from django.db import models
from users.models import User
from companies.models import Company

# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    email = models.EmailField()
    company_name = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL)
    mobile = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
