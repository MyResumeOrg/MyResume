# Generated by Django 5.0.6 on 2024-08-08 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_bi_customeruser_bi'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('organization_logo', models.FileField(blank=True, null=True, upload_to='organization_logos/')),
                ('organization_link', models.URLField()),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificate_files/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=35)),
                ('type_skill', models.CharField(choices=[('LANGUAGE', 'Language'), ('FRAMEWORK', 'Framework'), ('TOOL', 'Tool'), ('METHODOLOGY', 'Methodology'), ('SOFTWARE', 'Software'), ('DATABASE', 'Database'), ('CLOUD', 'Cloud'), ('LIBRARY', 'Library'), ('OPERATING_SYSTEM', 'Operating System'), ('DEVOPS', 'DevOps'), ('DATA_ANALYSIS', 'Data Analysis'), ('AI_ML', 'Artificial Intelligence / Machine Learning'), ('CYBER_SECURITY', 'Cyber Security'), ('NETWORKING', 'Networking'), ('PROJECT_MANAGEMENT', 'Project Management')], max_length=50)),
                ('self_avaliation', models.CharField(choices=[('BEGINNER', 'Beginner'), ('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('PROFICIENT', 'Proficient'), ('ADVANCED', 'Advanced'), ('EXPERT', 'Expert'), ('MASTER', 'Master')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituition_name', models.CharField(max_length=150)),
                ('instituition_logo', models.FileField(blank=True, null=True, upload_to='instituition_logos/')),
                ('instituition_link', models.URLField(blank=True, null=True)),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificate_files/')),
                ('title', models.CharField(max_length=100)),
                ('estimated_hours', models.IntegerField()),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
                ('used_skills', models.ManyToManyField(blank=True, to='experiences.hardskill')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('SPANISH', 'Spanish'), ('FRENCH', 'French'), ('GERMAN', 'German'), ('PORTUGUESE', 'Portuguese'), ('ITALIAN', 'Italian'), ('CHINESE', 'Chinese'), ('JAPANESE', 'Japanese'), ('KOREAN', 'Korean'), ('RUSSIAN', 'Russian'), ('ARABIC', 'Arabic'), ('HINDI', 'Hindi'), ('BENGALI', 'Bengali'), ('TURKISH', 'Turkish'), ('VIETNAMESE', 'Vietnamese'), ('THAI', 'Thai'), ('DUTCH', 'Dutch'), ('GREEK', 'Greek'), ('SWEDISH', 'Swedish'), ('NORWEGIAN', 'Norwegian'), ('DANISH', 'Danish')], max_length=50)),
                ('self_avaliation', models.CharField(choices=[('BEGINNER', 'Beginner'), ('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('PROFICIENT', 'Proficient'), ('ADVANCED', 'Advanced'), ('EXPERT', 'Expert'), ('MASTER', 'Master')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='OpenSourceContribuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('project_logo', models.FileField(blank=True, null=True, upload_to='project_logos/')),
                ('description', models.TextField(max_length=500)),
                ('repository_link', models.URLField()),
                ('project_link', models.URLField(blank=True, null=True)),
                ('solutions_commit_links', models.TextField()),
                ('used_skills', models.ManyToManyField(to='experiences.hardskill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=150)),
                ('organization_logo', models.FileField(blank=True, null=True, upload_to='organization_logos/')),
                ('organization_link', models.URLField()),
                ('responsibility', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('used_skills', models.ManyToManyField(to='experiences.hardskill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=70)),
                ('responsible_foto', models.FileField(blank=True, null=True, upload_to='responsible_fotos/')),
                ('responsible_linkedin', models.URLField()),
                ('recomendation_text', models.TextField(max_length=700)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='RelevantProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('project_logo', models.FileField(blank=True, null=True, upload_to='project_logos/')),
                ('description', models.TextField(max_length=500)),
                ('repository_link', models.URLField()),
                ('project_link', models.URLField(blank=True, null=True)),
                ('used_skills', models.ManyToManyField(to='experiences.hardskill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=35)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser')),
            ],
        ),
    ]