from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/user/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/mechanic/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('request-help/', views.create_service_request, name='create_service_request'),
    path('request/<int:pk>/', views.request_details, name='request_details'),
]