from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login_view, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Mechanic Management
    path('mechanics/', views.mechanic_list, name='mechanic_list'),
    path('mechanics/approve/<int:pk>/', views.approve_mechanic, name='approve_mechanic'),
    
    # Request Monitoring
    path('requests/', views.admin_request_view, name='admin_request_view'),
]