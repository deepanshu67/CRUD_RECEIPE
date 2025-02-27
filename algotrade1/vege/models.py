from django.db import models
from .models import *

# Create your models here.

class receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description=models.CharField(max_length=200)
    receipe_image=models.ImageField(upload_to='receipeimage')

    