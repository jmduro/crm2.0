from django.db import models
from users.models import User
from companies.models import Company
from contacts.models import Contact


# Create your models here.


class Deal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal_name = models.CharField(max_length=50, unique=True)
    contact_name = models.ForeignKey(Contact, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    closing_date = models.DateField()
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.deal_name}'
