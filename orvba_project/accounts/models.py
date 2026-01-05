from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Role-based boolean flags
    is_customer = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class MechanicProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='mechanic_profile')
    
    # Location of the workshop (Static location)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    
    address = models.TextField()
    
    # Verification Documents
    id_proof = models.ImageField(upload_to='mechanic_ids/')
    
    # Approval Status (Managed by Admin)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Mechanic: {self.user.username}"