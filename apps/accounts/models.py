from django.db import models
from django.contrib.auth.models import User


class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_data = models.DateField(blank= False)

