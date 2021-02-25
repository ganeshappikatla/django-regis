from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Enters(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)

class Login(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
