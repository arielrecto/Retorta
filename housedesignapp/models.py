from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Inbox(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=20, null=True)
    message = models.TextField(max_length=255, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    



class Project(models.Model):
    image = models.ImageField(null=True, upload_to="image")
    name = models.CharField(max_length=20, null=True)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], null=True)
    description = models.TextField(max_length=255, null=True)
    
    def __str__(self):
        return self.name



class Appointment(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        REJECT = 'REJECT'
        APPROVE = 'APPROVED'
    
    email = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    contact_number = models.PositiveIntegerField(validators=[MaxValueValidator(11)], null=True)
    status = models.CharField(max_length=20, default=Status.PENDING, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
