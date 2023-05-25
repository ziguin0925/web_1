from django.db import models
from common.models import User

# Create your models here.

class Post(models.Model):
    postname=models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    create_date =models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    
class mention(models.Model):
    price = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)
    distance = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    importance = models.CharField(max_length=10)
    mention_FK = models.ForeignKey(User,on_delete=models.CASCADE)