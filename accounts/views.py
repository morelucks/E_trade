from django.shortcuts import render
from .form import RegistrationForm
from accounts.models import Account
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return HttpResponse("User created successfully.")
        else:
            # Print form errors for debugging
            print(form.errors)

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return 