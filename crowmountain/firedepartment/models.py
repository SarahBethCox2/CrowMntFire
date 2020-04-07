from django.db import models
import uuid

# Create your models here.

class Citizen(models.Model):
    CitizenID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=50, null=True)
    Last_Name =  models.CharField(max_length=50, null=True)
    Phone = models.CharField(max_length=10,null=True)
    Address = models.CharField(max_length=100, null=True)
    Age = models.IntegerField(null=True)
    Email = models.EmailField(max_length=30, null=True)
class Volunteer(models.Model):
    status =(
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    )
    Citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    Acceptance_Status = models.CharField(max_length=50, null=True, choices=status)
    Date_Form_Submitted = models.DateField(auto_now_add=True, null=True)
     