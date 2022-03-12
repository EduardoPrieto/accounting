from django.db import models
from company.models import Company


# Create your models here.
class Expenses(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateField()
    invoice = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Sales(models.Model):

    date = models.DateField()
    payment_type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.price

class AccountingBreak(models.Model):

    date_start = models.DateField()
    date_finish = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


