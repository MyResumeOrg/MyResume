from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.experiences.forms import * 


@login_required(login_url='/accounts/login/')
def add_experiences(request):
    user = get_object_or_404(User, username=request.user.username)
    customer_user = get_object_or_404(CustomerUser, user=user.id)
    hardskill_form = HardSkillForm()
    softskill_form = SoftSkillForm()
    certification_form = CertificationForm(customer=customer_user.id)
    professional_experience_form = ProfessionalExperienceForm(customer=customer_user.id)
    academic_experience_form = AcademicExperienceForm()
    relevant_project_form = RelevantProjectForm(customer=customer_user.id)
    recomendation_form = RecomendationForm()
    open_source_contribuition_form = OpenSourceContribuitionForm(customer=customer_user.id)
    language_form = LanguageForm()
    
    if request.method == 'POST':
        submit_value = request.POST.get("submit_button")
        print(submit_value)

        if submit_value == 'Hard Skill':
            hardskill_form = HardSkillForm(request.POST, request.FILES)  
            if hardskill_form.is_valid():
                hardskill = hardskill_form.save(commit=False)
                hardskill.customer_id = customer_user.id  
                hardskill.save()
                messages.success(request, 'Hard Skill registred sucefuly.')
                return redirect('add_experiences')
                
        elif submit_value == 'Soft Skill':
            softskill_form = SoftSkillForm(request.POST)
            if softskill_form.is_valid():
                softskill = softskill_form.save(commit=False)
                softskill.customer_id = customer_user.id
                softskill.save()
                messages.success(request, 'Soft Skill registred sucefuly.')
                return redirect('add_experiences')
        
        elif submit_value == 'Certification':
            certification_form = CertificationForm(request.POST, request.FILES)
            if certification_form.is_valid():
                certification = certification_form.save(commit=False)
                certification.customer_id = customer_user.id
                certification.save()
                certification_form.save_m2m()

                messages.success(request, 'Certification registred sucefuly.')
                return redirect('add_experiences')
        
        elif submit_value == 'Professional Experience':
            professional_experience_form = ProfessionalExperienceForm(request.POST, request.FILES)
            if professional_experience_form.is_valid():
                professional_experience = professional_experience_form.save(commit=False)
                professional_experience.customer_id = customer_user.id
                professional_experience.save()
                professional_experience_form.save_m2m()

                messages.success(request, 'Professional Experience registred sucefuly.')
                return redirect('add_experiences')
            else:
                print(professional_experience_form.errors)

            
        elif submit_value == 'Academic Experience':
            academic_experience_form = AcademicExperienceForm(request.POST, request.FILES)
            if academic_experience_form.is_valid():
                academic_experience = academic_experience_form.save(commit=False)
                academic_experience.customer_id = customer_user.id
                academic_experience.save()
                messages.success(request, 'Academic Experience registred sucefuly.')
                return redirect('add_experiences')

        elif submit_value == 'Relevant Project':
            relevant_project_form = AcademicExperienceForm(request.POST, request.FILES)
            if relevant_project_form.is_valid():
                relevant_project = relevant_project_form.save(commit=False)
                relevant_project.customer_id = customer_user.id
                relevant_project.save()
                relevant_project_form.save_m2m()

                messages.success(request, 'Relevant Project registred sucefuly.')
                return redirect('add_experiences')
            
        elif submit_value == 'Recomendation':
            recomendation_form = RecomendationForm(request.POST, request.FILES)
            if recomendation_form.is_valid():
                recomendation = recomendation_form.save(commit=False)
                recomendation.customer_id = customer_user.id
                recomendation.save()
                messages.success(request, 'Recomendation registred sucefuly.')
                return redirect('add_experiences')
                
        elif submit_value == 'Open Source Contribuition':
            open_source_contribuition_form = OpenSourceContribuitionForm(request.POST, request.FILES)
            if open_source_contribuition_form.is_valid():
                open_source_contribuition = open_source_contribuition_form.save(commit=False)
                open_source_contribuition.customer_id = customer_user.id
                open_source_contribuition.save()
                open_source_contribuition_form.save_m2m()

                messages.success(request, 'Open Source Contribuition registred sucefuly.')
                return redirect('add_experiences')
            
        elif submit_value == 'Language':
            language_form = LanguageForm(request.POST)
            if language_form.is_valid():
                language = language_form.save(commit=False)
                language.customer_id = customer_user.id
                language.save()
                messages.success(request, 'Language registred sucefuly.')
                return redirect('add_experiences')
                
    else:
        hardskill_form = HardSkillForm()
        softskill_form = SoftSkillForm()
        certification_form = CertificationForm(customer= customer_user.id)
        professional_experience_form = ProfessionalExperienceForm(customer= customer_user.id)
        academic_experience_form = AcademicExperienceForm()
        relevant_project_form = RelevantProjectForm(customer= customer_user.id)
        recomendation_form = RecomendationForm()
        open_source_contribuition_form = OpenSourceContribuitionForm(customer= customer_user.id)
        language_form = LanguageForm()

    return render(request, 'experiences/add_experiences.html', {'forms': [hardskill_form, softskill_form, certification_form, professional_experience_form, academic_experience_form, relevant_project_form, recomendation_form, open_source_contribuition_form, language_form]})


@login_required(login_url='/accounts/login/')
def my_experiences(request):
    user = get_object_or_404(User, username=request.user.username)
    customer_user = get_object_or_404(CustomerUser, user=user.id)

    user_hard_skills = HardSkill.objects.filter(customer=customer_user.id)
    user_soft_skills = SoftSkill.objects.filter(customer=customer_user.id)
    user_certifications = Certification.objects.filter(customer=customer_user.id)
    user_professional_experiences = ProfessionalExperience.objects.filter(customer=customer_user.id)
    user_academic_experiences = AcademicExperience.objects.filter(customer=customer_user.id)
    user_relevant_projects = RelevantProject.objects.filter(customer=customer_user.id)
    user_recommendations = Recommendation.objects.filter(customer=customer_user.id)
    user_open_source_contribuitions = OpenSourceContribuition.objects.filter(customer=customer_user.id)
    user_languages = Language.objects.filter(customer=customer_user.id)

    is_empty = not (user_hard_skills and user_soft_skills and user_certifications and user_professional_experiences and user_academic_experiences and user_relevant_projects and user_recommendations and user_open_source_contribuitions and user_languages)
    
    return render(request, 'experiences/my_experiences.html', {
        'hard_skills' : user_hard_skills, 
        'soft_skills' : user_soft_skills, 
        'certifications' : user_certifications,
        'professional_experiences' : user_professional_experiences,
        'academic_experiences' : user_academic_experiences,
        'relevant_projects' : user_relevant_projects,
        'recommendations' : user_recommendations,
        'open_source_contribuitions' : user_open_source_contribuitions,
        'languages' : user_languages,
        'is_empty' : is_empty
    })


@login_required(login_url='/accounts/login/')
def delete_experiences(request, experience_id):
    if request.method == 'POST':
        Model = apps.get_model('experiences', request.POST.get('model_name'))
        experience = get_object_or_404(Model, id=experience_id)
        experience.delete()
        
        messages.success(request, 'Experience deleted successfully.')
        return redirect('my_experiences')

