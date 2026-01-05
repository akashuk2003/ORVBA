from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .decorators import admin_required
from accounts.models import CustomUser, MechanicProfile
from services.models import ServiceRequest

# 1. Admin Login View
def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_admin or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "You are not authorized to access the Admin Panel.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin_panel/login.html', {'form': form})

# 2. Dashboard View (Stats)
@admin_required
def admin_dashboard(request):
    # Fetch Counts for the Dashboard
    total_users = CustomUser.objects.filter(is_customer=True).count()
    total_mechanics = CustomUser.objects.filter(is_mechanic=True).count()
    pending_approvals = MechanicProfile.objects.filter(is_approved=False).count()
    active_requests = ServiceRequest.objects.filter(status='Pending').count()

    context = {
        'total_users': total_users,
        'total_mechanics': total_mechanics,
        'pending_approvals': pending_approvals,
        'active_requests': active_requests
    }
    return render(request, 'admin_panel/dashboard.html', context)

# 3. View All Mechanics & Approval Logic
@admin_required
def mechanic_list(request):
    mechanics = MechanicProfile.objects.all().select_related('user')
    return render(request, 'admin_panel/mechanic_list.html', {'mechanics': mechanics})

@admin_required
def approve_mechanic(request, pk):
    mechanic = get_object_or_404(MechanicProfile, pk=pk)
    mechanic.is_approved = True
    mechanic.save()
    messages.success(request, f"{mechanic.user.username} has been approved.")
    return redirect('mechanic_list')

# 4. View All Service Requests (Monitoring)
@admin_required
def admin_request_view(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/request_list.html', {'requests': requests})