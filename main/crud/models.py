from pyexpat import model
from statistics import mode
from urllib import request
from django.db import models

# Create your models here.


class course(models.Model):
    name = models.CharField(max_length=50)

class std(models.Model):
    name = models.CharField(max_length=50)
    c_name = models.CharField(max_length=55)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    