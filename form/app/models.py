from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100,blank=True)
    age = models.CharField(max_length=100)
    dob = models.DateField()
    active = models.BooleanField(default=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
