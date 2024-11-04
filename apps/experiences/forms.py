from django import forms 
from apps.experiences.models import * 

from django import forms

class BaseFormWithTitle(forms.ModelForm):
    form_title = "Default Form Title"  

    def __init__(self, *args, **kwargs):
        super(BaseFormWithTitle, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label

            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{existing_classes} form_input".strip()

            if isinstance(field.widget, forms.Select):
                field.choices = [('', 'Select an option')] + list(field.choices)  


    def get_title(self):
        return f'<h3>Add {self.form_title}</h3>'

    def get_form_value(self):
        return f'{self.form_title}'
    
    def get_id_content(self):
        return self.form_title.replace(' ', '_').lower()

class HardSkillForm(BaseFormWithTitle):
    form_title = 'Hard Skill'
    class Meta:
        model = HardSkill
        exclude = ['customer']
        widgets = {
            'skill_image': forms.FileInput(attrs={'class': 'image_input'}),
        }
        labels = {
            'skill': 'Skill',
            'type_skill': 'Type',
            'self_avaliation': 'Self avaliation',
            'skill_image': 'Skill logo'
        }


class SoftSkillForm(BaseFormWithTitle):
    form_title = 'Soft Skill'
    class Meta:
        model = SoftSkill
        exclude = ['customer']
        labels = {
            'skill' : 'Soft Skill'
        }

class CertificationForm(BaseFormWithTitle):
    form_title = 'Certification'
    class Meta:
        model = Certification
        exclude = ['customer']
        widgets = {
            'certificate_file': forms.FileInput(attrs={'class': 'image_input'}),
            'instituition_logo': forms.FileInput(attrs={'class': 'image_input'}),
            'used_skills': forms.CheckboxSelectMultiple(attrs={'class': 'multiple_checkbox_input'}),
        }
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

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

        if customer:
            self.fields['used_skills'].queryset = HardSkill.objects.filter(customer=customer)

class ProfessionalExperienceForm(BaseFormWithTitle):
    form_title = 'Professional Experience'

    class Meta:
        model = ProfessionalExperience
        exclude = ['customer']
        widgets = {
            'organization_logo': forms.FileInput(attrs={'class':'image_input'}),
            'used_skills': forms.CheckboxSelectMultiple(attrs={'class':'multiple_checkbox_input'}),
        }
        labels = {
            'organization_name':'Organization name',
            'organization_logo':'Organization logo',
            'organization_link':'Organization link',
            'responsibility':'Responsability',
            'used_skills':'Used Skills',
            'description':'Description',
            'start_date':'Start date',
            'end_date':'End date'
        }

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

        if customer:
            self.fields['used_skills'].queryset = HardSkill.objects.filter(customer=customer)


class AcademicExperienceForm(BaseFormWithTitle):
    form_title = 'Academic Experience'

    class Meta:
        model = AcademicExperience
        exclude = ['customer']
        widgets = {
            'organization_logo': forms.FileInput(attrs={'class': 'image_input'}),
            'certificate_file': forms.FileInput(attrs={'class': 'image_input'}),
        }
        labels = {
            'organization_name':'Organization name',
            'organization_logo':'Organization logo',
            'organization_link':'Organization link',
            'certificate_file':'Certificate file',
            'title':'Title',
            'description':'Description',
            'start_date':'Start date',
            'end_date':'End date'
        }


class RelevantProjectForm(BaseFormWithTitle):
    form_title = 'Relevant Project'

    class Meta:
        model = RelevantProject
        exclude = ['customer']
        widgets = {
            'project_logo': forms.FileInput(attrs={'class': 'image_input'}),
            'used_skills': forms.CheckboxSelectMultiple(attrs={'class': 'multiple_checkbox_input'}),
        }
        labels = {
            'title':'Title',
            'project_logo':'Project logo',
            'used_skills':'Used Skills',
            'description':'Description',
            'repository_link':'Repository link',
            'project_link':'Project link'
        }

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

        if customer:
            self.fields['used_skills'].queryset = HardSkill.objects.filter(customer=customer)


class RecomendationForm(BaseFormWithTitle):
    form_title = 'Recomendation'

    class Meta:
        model = Recommendation
        exclude = ['customer']
        widgets = {
            'responsible_foto': forms.FileInput(attrs={'class': 'image_input'}),
        }
        labels = {
            'responsible':'Responsible',
            'responsible_foto':'Responsible photo',
            'responsible_linkedin':'Responsible LinkedIn',
            'recomendation_text':'Recomendation text'
        }

class OpenSourceContribuitionForm(BaseFormWithTitle):
    form_title = 'Open Source Contribuition'

    class Meta:
        model = OpenSourceContribuition
        exclude = ['customer']

        widgets = {
            'project_logo': forms.FileInput(attrs={'class':'image_input'}),
            'used_skills': forms.CheckboxSelectMultiple(attrs={'class':'multiple_checkbox_input'}),
        }
        labels = {
            'title':'Title',
            'project_logo':'Project logo',
            'used_skills':'Used Skills',
            'description':'Description',
            'repository_link':'Repository link',
            'project_link':'Project link',
            'solutions_commit_links':'Solutions commit links'
        }

    def __init__(self, *args, **kwargs):
        customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

        if customer:
            self.fields['used_skills'].queryset = HardSkill.objects.filter(customer=customer)

class LanguageForm(BaseFormWithTitle):
    form_title = 'Language'

    class Meta:
        model = Language
        exclude = ['customer']

    labels = {
        'language':'Language',
        'self_avaliation':'Self avaliation'
    }
