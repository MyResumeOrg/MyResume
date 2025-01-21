from django import forms
from apps.accounts.models import BI, CustomerUser
from django.contrib.auth.models import User
from datetime import date


class LoginForms(forms.Form):
    login_email = forms.EmailField(
        label= 'E-mail',
        required= True,
        max_length= 200,
        widget= forms.EmailInput(
            attrs={
                'class':'form_input',
                'placeholder':'E-mail'
            }
        )
    )

    password = forms.CharField(
        label= 'Password',
        required= True,
        max_length= 100,
        widget= forms.PasswordInput(
            attrs={
                'class':'form_input',
                'placeholder':'Password'
            }
        )
    
    )   


class RegisterForms(forms.Form):
    first_name = forms.CharField(
        label= 'First name',
        required= True,
        max_length= 70,
        widget= forms.TextInput(
            attrs = {
                'class':'form_input',
                'placeholder':'First name'
            }
        )
    )

    last_name = forms.CharField(
        label= 'Last name',
        required= True,
        max_length= 70,
        widget= forms.TextInput(
            attrs = {
                'class':'form_input',
                'placeholder':'Last name'
            }
        )
    )

    birth_data = forms.DateField(
        label= 'Date of birth',
        required= True,
        widget= forms.DateInput(
            attrs= {
                'class':'form_input',
                'type':'date',
                'placeholder':'MM/DD/YYYY'
            }
        )
    )

    username = forms.CharField(
        label= 'Username',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs= {
                'class':'form_input',
                'placeholder':'Username'
            }
        )
    )

    register_email = forms.EmailField(
        label= 'Email',
        required= True,
        max_length= 200,
        widget= forms.EmailInput(
            attrs= {
                'class':'form_input',
                'placeholder':'name@example.com'
            }
        )
    )

    email_confirmation = forms.EmailField(
        label='Email confirmation',
        required= True,
        max_length= 200,
        widget= forms.EmailInput(
            attrs= {
                'class':'form_input',
                'placeholder':'Confirm your email'
            }
        )
    )

    password = forms.CharField(
        label= 'Password',
        required= True,
        max_length= 100,
        widget= forms.PasswordInput(
            attrs={
                'class':'form_input',
                'placeholder':'Password'
            }
        )
    )

    password_confirmation = forms.CharField(
        label= 'Password confirmation',
        required= True,
        max_length= 100,
        widget= forms.PasswordInput(
            attrs= {
                'class':'form_input',
                'placeholder':'Password confirmation'
            }
        )
    )
             

    def clean(self):
        cleaned_data = super().clean()

        username = self.cleaned_data.get('username')
        register_email = self.cleaned_data.get('register_email')
        email_confirmation = self.cleaned_data.get('email_confirmation')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        birth_data = self.cleaned_data.get('birth_data')

        if username:
            username = username.strip()
            if ' ' in username:
                raise forms.ValidationError('It is not possible to contain spaces in the username.')
        else:
            return username
        
        if birth_data > date.today(): # Tested and approved
            raise forms.ValidationError('Birth date cannot be in the future.')

        if register_email and email_confirmation:
            if register_email != email_confirmation:
                raise forms.ValidationError('Email and email confirmation must be the same.')
            
        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError('Password and password confirmation must be the same.')

        return cleaned_data

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form_input blur_input'}),
            'last_name': forms.TextInput(attrs={'class': 'form_input blur_input'}),
            'email': forms.EmailInput(attrs={'class': 'form_input blur_input'}),
        }
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email'
        }
            
class BIForm(forms.ModelForm):
    
    class Meta:
        model = BI
        fields = '__all__'
        
        widgets = {
            'linkedin_url': forms.URLInput(attrs={'class': 'form_input blur_input'}),
            'github_url': forms.URLInput(attrs={'class': 'form_input blur_input'}),
            'x_url': forms.URLInput(attrs={'class': 'form_input blur_input'}),
            'city_of_residence': forms.TextInput(attrs={'class' : 'form_input blur_input'}),
            'areas_of_expertise': forms.TextInput(attrs={'class' : 'form_input blur_input'}),
            'professional_bio': forms.Textarea(attrs={'class' : 'form_input blur_input'}),

        }
        labels = {
            'linkedin_url': 'LinkedIn',
            'github_url': 'GitHub',
            'x_url': 'X (Twitter)',
            'professional_bio': 'Professional biography'
        }

class CustomerUserForm(forms.ModelForm):
    
    class Meta:
        model = CustomerUser
        fields = ('profile_image',)

        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'file_input'}),
        }
        labels = {
            'profile_image': 'Profile image',
        }
