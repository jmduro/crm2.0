from django.db import models

# Create your models here.


class Company(models.Model):

    company_name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=25, blank=True)
    website = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=250, blank=True)
    billing_street = models.CharField(max_length=50, blank=True)
    billing_city = models.CharField(max_length=50, blank=True)
    billing_state = models.CharField(max_length=50, blank=True)
    billing_country = models.CharField(max_length=50, blank=True)
    billing_code = models.CharField(max_length=20, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company_name}'
