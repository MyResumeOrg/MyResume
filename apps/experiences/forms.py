from django import forms 
from apps.experiences.models import * 

from django import forms

class BaseFormWithTitle(forms.ModelForm):
    form_title = "Default Form Title"  

    def __init__(self, *args, **kwargs):
        super(BaseFormWithTitle, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['class'] = 'form_input'

            if isinstance(field.widget, forms.Select):
                field.choices = [('', 'Select an option')] + list(field.choices)

            field.label = ''  


    def get_title(self):
        return f'<h3>{self.form_title}</h3>'

class HardSkillForm(BaseFormWithTitle):
    form_title = 'Add Hard Skill'
    class Meta:
        model = HardSkill
        exclude = ['customer']


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