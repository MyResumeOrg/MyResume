from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import login, register, terms_of_use

urlpatterns = [
   path('login/', login, name='login'),
   path('register/', register, name='register'),
   path('terms_of_use/', terms_of_use, name='terms_of_use')
]
