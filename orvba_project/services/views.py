from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from django.core.exceptions import ObjectDoesNotExist
@login_required
def user_dashboard(request):
    # Show user's history
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'user/dashboard.html', {'requests': requests})



@login_required
def mechanic_dashboard(request):
    mechanic_profile = request.user.mechanic_profile
    
    # 1. Check Approval
    if not mechanic_profile.is_approved:
        return render(request, 'mechanic/wait_approval.html')
        
    # 2. Fetch "Available Jobs" (Pending requests with NO mechanic assigned)
    available_jobs = ServiceRequest.objects.filter(status='Pending', mechanic__isnull=True).order_by('-created_at')
    
    # 3. Fetch "My Active Jobs" (Requests assigned to THIS mechanic)
    my_tasks = ServiceRequest.objects.filter(mechanic=request.user).order_by('-created_at')
    
    context = {
        'available_jobs': available_jobs,
        'tasks': my_tasks
    }
    
    return render(request, 'mechanic/dashboard.html', context)

from .forms import ServiceRequestForm
from django.contrib import messages

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.status = 'Pending'
            service_request.save()
            messages.success(request, "Help is on the way! Request submitted.")
            return redirect('user_dashboard')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'user/request_help.html', {'form': form})

@login_required
def request_details(request, pk):
    # Ensure only mechanics can view this
    if not request.user.is_mechanic:
        return redirect('user_dashboard')
        
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        # Logic to Accept/Complete request
        action = request.POST.get('action')
        if action == 'accept':
            service_request.mechanic = request.user
            service_request.status = 'Accepted'
        elif action == 'complete':
            service_request.status = 'Completed'
        service_request.save()
        return redirect('mechanic_dashboard')

    return render(request, 'mechanic/request_details.html', {'req': service_request})


@login_required
def mechanic_dashboard(request):
    # SAFETY CHECK: Ensure the user is actually marked as a mechanic
    if not request.user.is_mechanic:
        # If an Admin or Customer tries to access this page, send them away
        return redirect('user_dashboard')

    try:
        # Try to get the profile
        mechanic_profile = request.user.mechanic_profile
    except ObjectDoesNotExist:
        return render(request, 'base.html', {
            'content': "Error: Your account is marked as 'Mechanic' but has no Profile data. Please contact Admin or re-register."
        })

    # 1. Check Approval
    if not mechanic_profile.is_approved:
        return render(request, 'mechanic/wait_approval.html')
        
    # 2. Fetch "Available Jobs" (Pending requests with NO mechanic assigned)
    available_jobs = ServiceRequest.objects.filter(status='Pending', mechanic__isnull=True).order_by('-created_at')
    
    # 3. Fetch "My Active Jobs" (Requests assigned to THIS mechanic)
    my_tasks = ServiceRequest.objects.filter(mechanic=request.user).order_by('-created_at')
    
    context = {
        'available_jobs': available_jobs,
        'tasks': my_tasks
    }
    
    return render(request, 'mechanic/dashboard.html', context)