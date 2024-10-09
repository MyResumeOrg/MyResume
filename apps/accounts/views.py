# from apps.accounts.forms import LoginForms, CadastroForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from apps.accounts.forms import LoginForms, RegisterForms
from django.contrib import messages
from apps.accounts.models import CustomerUser

def terms_of_use(request):
    return render(request, 'accounts/terms_of_use.html')

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['login_email'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                username= email,
                password= password
            )

            if user:
                messages.success(request, 'Login completed successfully.')
                auth.login(request, user)
                return redirect('add_experiences')
            
            messages.error(request, 'Invalid email or password.')
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForms()
        return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
            birth_data = form['birth_data'].value()
            username = form['username'].value()
            email = form['register_email'].value()
            password = form['password'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'accounts/register.html', { 'form': form })
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'accounts/register.html', { 'form': form })
            
            user = User.objects.create_user(
                username= username,
                first_name= first_name,
                last_name= last_name,
                email= email,
                password= password
            )

            user.save()

            extended_user = CustomerUser.objects.create(
                user= user,
                birth_data= birth_data,
            )

            extended_user.save()

            messages.success(request, 'Registration completed successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid form submission.')
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForms()
        return render(request, 'accounts/register.html', { 'form': form })
