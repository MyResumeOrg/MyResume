# from apps.accounts.forms import LoginForms, CadastroForms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from apps.accounts.forms import LoginForms, RegisterForms, BIForm, CustomerUserForm, UserForm
from django.contrib import messages
from apps.accounts.models import CustomerUser, BI
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


def terms_of_use(request):
    return render(request, 'accounts/terms_of_use.html')

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
    
        if form.is_valid():
            email = form.cleaned_data.get('login_email')
            password = form.cleaned_data.get('password')

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
            for error in form.errors.values():
                messages.error(request, error)
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
            for error in form.errors.values():
                messages.error(request, error)
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForms()
        return render(request, 'accounts/register.html', { 'form': form })


@login_required(login_url='/accounts/login/') 
def profile_page(request):
    user = request.user
    customer_user = CustomerUser.objects.filter(user=user.id).first()
    bi_informations = BI.objects.filter(id=customer_user.bi_id).first() if customer_user else None

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        customer_form = CustomerUserForm(request.POST, request.FILES, instance=customer_user)
        bi_form = BIForm(request.POST, instance=bi_informations)
        
        if user_form.is_valid() and bi_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            bi_form.save()

            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_page')
        else:
            messages.error(request, 'There was an error updating your profile. Please check the information entered.')
            return redirect('profile_page')

    if bi_informations:
        bi_form = BIForm(initial={'linkedin_url': bi_informations.linkedin_url, 'github_url': bi_informations.github_url, 'x_url' : bi_informations.x_url, 'city_of_residence': bi_informations.city_of_residence, 'areas_of_expertise': bi_informations.areas_of_expertise, 'professional_bio': bi_informations.professional_bio })
    else:
        bi_form = BIForm()
        
    customer_form = CustomerUserForm(initial={'profile_image': customer_user.profile_image})
    user_form = UserForm(initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})

    return render(request, 'accounts/profile_page.html', {
        'user' : user,
        'customer_user' : customer_user, 
        'bi' : bi_informations,
        'user_form' : user_form,
        'customer_form' : customer_form,
        'bi_form' : bi_form
    })
