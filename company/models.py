from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name



class User_Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=100, default='Director')
