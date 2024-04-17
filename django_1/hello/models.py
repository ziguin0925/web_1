from django.db import models
from common.models import User

# Create your models here.

class Post(models.Model):
    postname=models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    create_date =models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    
class Mention(models.Model):
    price = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)
    distance = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    importance = models.CharField(max_length=10)
    User_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='User_id')





class Recom(models.Model):
    img1=models.CharField(max_length=1000)
    img2=models.CharField(max_length=1000)
    link1=models.CharField(max_length=1000)
    link2=models.CharField(max_length=1000)
    num=models.CharField(max_length=5)
