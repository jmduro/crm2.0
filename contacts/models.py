from django.db import models
from users.models import User
from companies.models import Company

# Create your models here.


class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    company_name = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.SET_NULL)
    mobile = models.CharField(max_length=25, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    home_phone = models.CharField(max_length=25, blank=True)
    email_opt_out = models.EmailField(blank=True)
    description = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
