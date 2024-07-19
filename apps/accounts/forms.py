from django import forms

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

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            username = username.strip()
            if ' ' in username:
                print('nome vazio')
                raise forms.ValidationError('It is not possible to contain spaces in the username.')
        else:
            return username
        
    def confirming_email(self):
        register_email = self.cleaned_data.get('register_email')
        email_confirmation = self.cleaned_data.get('email_confirmation')

        if register_email and email_confirmation:
            if register_email != email_confirmation:
                raise forms.ValidationError('Email and email confirmation must be the same.')
            else:
                return register_email
    
    def confirming_password(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError('Password and password confirmation must be the same.')
            else:
                return password
