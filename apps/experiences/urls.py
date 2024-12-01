# from django.contrib import admin
from django.urls import path
from apps.experiences.views import add_experiences, my_experiences, delete_experiences

urlpatterns = [
   path('add_experiences/', add_experiences, name='add_experiences'),
   path('my_experiences/', my_experiences, name='my_experiences'),
   path('delete_experiences/<int:experience_id>/', delete_experiences, name='delete_experiences')
]
