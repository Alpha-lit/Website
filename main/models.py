from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Account creation

class CustomUser(AbstractUser):
    email               = models.EmailField(unique=True)
    username            = models.CharField(max_length=200, unique=True)
    password            = models.CharField(max_length=400)

#Email automatoin stuff
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     # Add other fields as per your requirements

#     def __str__(self):
#         return self.name
    
# class Purchase(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100)
#     purchase_date = models.DateField()
#     # Add other fields as per your requirements

#     def __str__(self):
#         return self.product_name
    
# class Email(models.Model):
#     recipient = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=200)
#     content = models.TextField()
#     sent_date = models.DateTimeField(auto_now_add=True)
#     # Add other fields as per your requirements

#     def __str__(self):
#         return self.subject