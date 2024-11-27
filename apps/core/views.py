from django.shortcuts import render

def index(request):
    return render(request, 'core/home.html')

def building(request):
    is_owner = True if request.user.is_authenticated else False
    return render(request, 'core/building.html', {'is_owner' : is_owner})