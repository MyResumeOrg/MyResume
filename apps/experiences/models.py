from django.db import models
from django.core.exceptions import ValidationError
from apps.accounts.models import CustomerUser
from os.path import splitext

def validate_image_file(value):
    ext = splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg', '.pdf']
    if ext not in valid_extensions:
        raise ValidationError(f'File type {ext} is not suported. Use {', '.join(valid_extensions)}')

POSSIBLE_SKILL_TYPES = [
    ('LANGUAGE', 'Language'),
    ('FRAMEWORK', 'Framework'),
    ('TOOL', 'Tool'),
    ('METHODOLOGY', 'Methodology'),
    ('SOFTWARE', 'Software'),
    ('DATABASE', 'Database'),
    ('CLOUD', 'Cloud'),
    ('LIBRARY', 'Library'),
    ('OPERATING_SYSTEM', 'Operating System'),
    ('DEVOPS', 'DevOps'),
    ('DATA_ANALYSIS', 'Data Analysis'),
    ('AI_ML', 'Artificial Intelligence / Machine Learning'),
    ('CYBER_SECURITY', 'Cyber Security'),
    ('NETWORKING', 'Networking'),
    ('PROJECT_MANAGEMENT', 'Project Management')
]

ACADEMIC_EXPERIENCES_TYPES = [
    ('GRADUATION', 'Graduation'),
    ('POSTGRADUATION', 'Postgraduation'),
    ('MASTERS', 'Master\'s Degree'),
    ('PHD', 'Ph.D.'),
    ('DIPLOMA', 'Diploma'),
    ('CERTIFICATE', 'Certificate'),
    ('ASSOCIATE', 'Associate Degree'),
    ('WORKSHOP', 'Workshop'),
    ('SEMINAR', 'Seminar'),
    ('ONLINE_COURSE', 'Online Course'),
    ('INTERNSHIP', 'Internship'),
    ('RESEARCH_PROJECT', 'Research Project'),
    ('EXCHANGE_PROGRAM', 'Exchange Program'),
    ('SHORT_COURSE', 'Short Course'),
    ('SPECIALIZATION', 'Specialization'),
]

SKILL_LEVEL = [
    ('BEGINNER', 'Beginner'),
    ('NOVICE', 'Novice'),
    ('INTERMEDIATE', 'Intermediate'),
    ('PROFICIENT', 'Proficient'),
    ('ADVANCED', 'Advanced'),
    ('EXPERT', 'Expert'),
    ('MASTER', 'Master')
]

POSSIBLES_LANGUAGES = [
    ('ENGLISH', 'English'),
    ('SPANISH', 'Spanish'),
    ('FRENCH', 'French'),
    ('GERMAN', 'German'),
    ('PORTUGUESE', 'Portuguese'),
    ('ITALIAN', 'Italian'),
    ('CHINESE', 'Chinese'),
    ('JAPANESE', 'Japanese'),
    ('KOREAN', 'Korean'),
    ('RUSSIAN', 'Russian'),
    ('ARABIC', 'Arabic'),
    ('HINDI', 'Hindi'),
    ('BENGALI', 'Bengali'),
    ('TURKISH', 'Turkish'),
    ('VIETNAMESE', 'Vietnamese'),
    ('THAI', 'Thai'),
    ('DUTCH', 'Dutch'),
    ('GREEK', 'Greek'),
    ('SWEDISH', 'Swedish'),
    ('NORWEGIAN', 'Norwegian'),
    ('DANISH', 'Danish'),
]

class HardSkill(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=35)
    type_skill = models.CharField(
        max_length= 50,
        choices=POSSIBLE_SKILL_TYPES
    )
    self_avaliation = models.CharField(
        max_length= 50,
        choices= SKILL_LEVEL
    )
    skill_image = models.FileField(
        upload_to='tecnologies_logos/',
        null=True,
        blank=True,
        validators=[validate_image_file]
    )

    def __str__(self):
        return self.skill


class SoftSkill(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=35)


class Certification(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    instituition_name = models.CharField(max_length= 150)
    instituition_logo = models.FileField(
        upload_to='instituition_logos/',
        null=True, 
        blank=True,
        validators=[validate_image_file]
    )
    instituition_link = models.URLField(null=True, blank=True)
    certificate_file = models.FileField(
        upload_to='certificate_files/',
        null=True,
        blank=True,
        validators=[validate_image_file]

    )
    title = models.CharField(max_length= 100)
    estimated_hours = models.IntegerField()
    description = models.TextField()
    used_skills = models.ManyToManyField(HardSkill, blank= True)

class ProfessionalExperience(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length= 150)
    organization_logo = models.FileField(
        upload_to='organization_logos/', 
        null=True, 
        blank=True,
        validators=[validate_image_file]
    )
    organization_link = models.URLField()
    responsibility = models.CharField(max_length= 70)
    used_skills = models.ManyToManyField(HardSkill)
    description = models.TextField(max_length= 500)
    start_date = models.DateField()
    end_date = models.DateField(blank= True, null=True)

    def clean(self):
        if self.end_date and self.end_date > self.start_date:
            raise ValidationError('An end date cannot be greater than a start date.') 

class AcademicExperience(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=100,)
    organization_logo = models.FileField(
        upload_to='organization_logos/', 
        null=True,
        blank= True,
        validators=[validate_image_file]
    )
    organization_link = models.URLField()
    certificate_file = models.FileField(
        upload_to= 'certificate_files/',
        null=True,
        blank=True,
        validators=[validate_image_file]
    )
    title = models.CharField(max_length= 50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class RelevantProject(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length= 35)
    project_logo = models.FileField(
        upload_to= 'project_logos/',
        null= True,
        blank= True,
        validators=[validate_image_file]
    )
    used_skills = models.ManyToManyField(HardSkill)
    description = models.TextField(max_length= 500)
    repository_link = models.URLField()
    project_link = models.URLField(null=True, blank=True)

class Recommendation(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    responsible = models.CharField(max_length= 70)
    responsible_foto = models.FileField(
        upload_to= 'responsible_fotos/',
        blank=True,
        null=True,
        validators=[validate_image_file]
    )
    responsible_linkedin = models.URLField()
    recomendation_text = models.TextField(max_length= 700)

class OpenSourceContribuition(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    project_logo = models.FileField(
        upload_to='project_logos/',
        null=True,
        blank=True,
        validators=[validate_image_file]
    )
    used_skills = models.ManyToManyField(HardSkill)
    description = models.TextField(max_length= 500)
    repository_link = models.URLField()
    project_link = models.URLField(null=True, blank=True)
    solutions_commit_links = models.TextField()

class Language(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices= POSSIBLES_LANGUAGES)
    self_avaliation = models.CharField(max_length=50, choices= SKILL_LEVEL)