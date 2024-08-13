from django.db import models
from django.core.exceptions import ValidationError
from apps.accounts.models import CustomerUser
# from apps.experiences.models import HardSkill, SoftSkill, Certification, ProfessionalExperience, AcademicExperience, RelevantProject, Recommendation,OpenSourceContribuition, Language


POSSIBLE_CHOICES = [
    ('HardSkill', 'Hard Skills'),
    ('SoftSkill', 'Soft Skills'),
    ('Certification', 'Certifications'),
    ('ProfessionalExperience', 'Professional experiences'),
    ('AcademicExperience', 'Academic experiences'),
    ('RelevantProject', 'Relevant projects'),
    ('Recommendation', 'Recommendations'),
    ('OpenSourceContribuition', 'Open source contribuitions'),
    ('Language', 'Languages')
]

class Sequence(models.Model):
    choice = models.CharField(max_length=50, choices=POSSIBLE_CHOICES, unique=True)

class Resume(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    sequences_of_informations = models.ManyToManyField(Sequence, blank=False, null=False)   

    def clean(self):
        if self.sequences_of_informations.count() == 0:
            raise ValidationError('At least one choice must be selected.')
        
        sequences_of_informations_ids = list(self.sequences_of_informations.values_list('id', flat=True))
        if len(sequences_of_informations_ids) != len(set(sequences_of_informations_ids)):
            raise ValidationError('There are duplicate choices in the list.')
