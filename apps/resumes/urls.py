from django.urls import path
from apps.resumes.views import resume_v1
from apps.core.views import building

urlpatterns = [
   path('basic/<str:username>/', resume_v1, name='basic'),
   path('complete/', building, name='complete')
]
