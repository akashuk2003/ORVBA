from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/mechanic/', views.register_mechanic, name='register_mechanic'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]