from django.shortcuts import render, redirect
# from apps.accounts.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from apps.accounts.forms import LoginForms, RegisterForms
from django.contrib import messages

def footer(request):
    return render(request, 'partials/footer.html')

def login(request):
    form = LoginForms()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    form = RegisterForms()
    return render(request, 'accounts/register.html', {'form': form})