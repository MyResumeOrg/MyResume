from django import forms 
from apps.experiences.models import * 

class HardSkillForm(forms.ModelForm):
    class Meta:
        model = HardSkill
        exclude = ['customer']
        labels = {
            'skill':'Skill',
            'type_skill':'Type Skill',
            'self_avaliation': 'Self avaliation'
        }

class SoftSkillForm(forms.ModelForm):
    class Meta:
        model = SoftSkill
        exclude = ['customer']
    labels = {
        'skill' : 'Soft Skill'
    }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = ['customer']
    labels = {
        'instituition_name':'Instituition name',
        'instituition_logo':'Instituition logo',
        'instituition_link':'Instituition link',
        'certificate_file':'Certificate file',
        'title':'Title',
        'estimated_hours':'Estimated hours',
        'description':'Description',
        'used_skills':'Used skills'
    }