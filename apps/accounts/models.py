from django.db import models
from django.contrib.auth.models import User

class BI(models.Model):
    linkedin_url = models.URLField(max_length=400, null=True, blank=True)
    github_url = models.URLField(max_length=400, null=True, blank=True)
    x_url = models.URLField(max_length=400, null=True, blank=True)
    city_of_residence = models.CharField(max_length=70, null=True, blank=True)
    areas_of_expertise = models.TextField(max_length=200, null=True, blank=True)
    professional_bio = models.TextField(max_length=600, null=True, blank=True)

class CustomerUser(models.Model):
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bi = models.OneToOneField(BI, on_delete=models.CASCADE, null=True, blank=True)
    birth_data = models.DateField()
