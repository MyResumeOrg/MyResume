from django.shortcuts import render
from apps.experiences.forms import * 

def add_experiences(request):
    form = HardSkillForm()
    return render(request, 'experiences/test.html', {'form' : form})