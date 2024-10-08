from django.urls import path
from apps.resumes.views import resume

urlpatterns = [
   path('<str:username>/', resume, name='resume'),
]
