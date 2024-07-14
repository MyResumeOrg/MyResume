from django import forms

class LoginForms(forms.Form):
    login_email = forms.EmailField(
        label= 'E-mail',
        required= True,
        max_length= 200,
        widget= forms.TextInput(
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
        widget= forms.TextInput(
            attrs= {
                'class':'form_input',
                'placeholder':'name@example.com'
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

