from django.db import models
from apps.accounts.models import CustomerUser

class BI(models.Model):
    customer = models.OneToOneField(CustomerUser, on_delete=models.SET_NULL, null=True)
    linkedin_url = models.URLField(max_length=400, null=True)
    github_url = models.URLField(max_length=400, null=True)
    x_url = models.URLField(max_length=400, null=True)
    city_of_residence = models.CharField(max_length=70, null=True)
    areas_of_expertise = models.TextField(max_length=200, null=True)
    professional_bio = models.TextField(max_length=600, null=True)
    