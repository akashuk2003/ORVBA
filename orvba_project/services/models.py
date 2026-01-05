from django.db import models
from django.conf import settings # Best practice to refer to User model

class ServiceRequest(models.Model):
    SERVICE_CHOICES = (
        ('Mechanic', 'Car Mechanic'),
        ('Towing', 'Towing Service'),
        ('Fuel', 'Fuel Delivery'),
    )
    
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    # Customer who requested help
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_requests')
    
    # Mechanic assigned (Can be null initially)
    mechanic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_requests')
    
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    
    # Precise Breakdown Location
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.service_type} Request by {self.customer.username} - {self.status}"