from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import footer, login, register

urlpatterns = [
   path('', footer),
   path('login/', login),
   path('register/', register)
]
