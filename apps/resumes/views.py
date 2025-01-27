from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.accounts.models import BI, CustomerUser
from apps.experiences.models import HardSkill
from django.contrib import messages

def resume_v1(request, username):
    user = get_object_or_404(User, username=username)
    customer_user = get_object_or_404(CustomerUser, user=user.id)
    bi_informations = BI.objects.get(id=customer_user.bi_id)

    if not all([bi_informations.linkedin_url, bi_informations.github_url,
                bi_informations.x_url, bi_informations.city_of_residence,
                bi_informations.areas_of_expertise, bi_informations.professional_bio]):
        messages.error(request, 'To access the basic resume, you need to add all Business informations first.')
        return redirect('profile_page')
    
    hard_skills = HardSkill.objects.filter(customer=customer_user.id)[:4]
    
    if request.user.is_authenticated:
        logged_username = request.user.username
        if logged_username == user.username:
            return render(request, 'resumes/resume_basic.html', {'user': user, 'customer_user' : customer_user, 'bi' : bi_informations, 'hard_skills' : hard_skills, 'is_owner': True})
    
    return render(request, 'resumes/resume_basic.html', {'user': user, 'customer_user' : customer_user, 'bi' : bi_informations, 'hard_skills' : hard_skills, 'is_owner': False})
