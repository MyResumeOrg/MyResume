from django.shortcuts import render

def index(request):
    return render(request, 'core/home.html')

def building(request):
    return render(request, 'core/building.html')