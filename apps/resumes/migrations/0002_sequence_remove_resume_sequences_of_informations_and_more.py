# Generated by Django 5.0.6 on 2024-08-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('HardSkill', 'Hard Skills'), ('SoftSkill', 'Soft Skills'), ('Certification', 'Certifications'), ('ProfessionalExperience', 'Professional experiences'), ('AcademicExperience', 'Academic experiences'), ('RelevantProject', 'Relevant projects'), ('Recommendation', 'Recommendations'), ('OpenSourceContribuition', 'Open source contribuitions'), ('Language', 'Languages')], max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='resume',
            name='sequences_of_informations',
        ),
        migrations.AddField(
            model_name='resume',
            name='sequences_of_informations',
            field=models.ManyToManyField(to='resumes.sequence'),
        ),
    ]
