from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import login, register, terms_of_use, profile_page

urlpatterns = [
   path('login/', login, name='login'),
   path('register/', register, name='register'),
   path('terms_of_use/', terms_of_use, name='terms_of_use'),
   path('profile/', profile_page, name='profile_page')
]
