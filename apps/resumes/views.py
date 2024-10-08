from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse

def resume(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponse('funcionou' + str(user))