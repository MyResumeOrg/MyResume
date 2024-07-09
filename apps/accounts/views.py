from django.shortcuts import render, redirect
# from apps.accounts.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def footer(request):
    return render(request, 'partials/footer.html')