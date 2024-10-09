from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.experiences.forms import * 

@login_required(login_url='/accounts/login/') 
def add_experiences(request):
    form = HardSkillForm()
    return render(request, 'experiences/add_experiences.html', {'form' : form})