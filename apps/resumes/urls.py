from django.urls import path
from apps.resumes.views import resume_v1

urlpatterns = [
   path('basic/<str:username>/', resume_v1, name='resume'),
]
