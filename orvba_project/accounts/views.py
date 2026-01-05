from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerSignUpForm, MechanicSignUpForm

def home(request):
    return render(request, 'home.html')
def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = CustomerSignUpForm()
    return render(request, 'accounts/register_customer.html', {'form': form})

def register_mechanic(request):
    if request.method == 'POST':
        # NOTE: request.FILES is needed for image upload
        form = MechanicSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mechanic_dashboard')
    else:
        form = MechanicSignUpForm()
    return render(request, 'accounts/register_mechanic.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # SMART REDIRECT
            if user.is_admin or user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_mechanic:
                return redirect('mechanic_dashboard')
            else:
                return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


from django.contrib.auth import logout # Make sure this is imported

def logout_view(request):
    logout(request)
    return redirect('home')