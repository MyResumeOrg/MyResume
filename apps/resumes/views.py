from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from apps.accounts.models import BI, CustomerUser
from apps.experiences.models import HardSkill

def resume_v1(request, username):
    user = get_object_or_404(User, username=username)
    customer_user = get_object_or_404(CustomerUser, user=user.id)
    bi_informations = get_object_or_404(BI, id=customer_user.bi_id)
    hard_skills = HardSkill.objects.filter(customer=customer_user.id)[:4]
    return render(request, 'resumes/resume_basic.html', {'user': user, 'customer_user' : customer_user, 'bi' : bi_informations, 'hard_skills' : hard_skills})