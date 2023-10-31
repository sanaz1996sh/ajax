from django.db import models

# Create your models here.
class registercls(models.Model):
    username=models.CharField(max_length=50)
    family=models.CharField(max_length=80)
    password=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)