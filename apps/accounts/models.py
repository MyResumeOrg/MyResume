from django.db import models
from django.contrib.auth.models import User

class BI(models.Model):
    linkedin_url = models.URLField(max_length=400, null=True)
    github_url = models.URLField(max_length=400, null=True)
    x_url = models.URLField(max_length=400, null=True)
    city_of_residence = models.CharField(max_length=70, null=True)
    areas_of_expertise = models.TextField(max_length=200, null=True)
    professional_bio = models.TextField(max_length=600, null=True)

class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bi = models.OneToOneField(BI, on_delete=models.CASCADE)
    birth_data = models.DateField(blank= False)

