
# Create your models here.
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, AbstractBaseUser
)
    
class User(AbstractUser):
    phone_number = models.CharField(max_length=12)
    birth_id1= models.CharField(max_length=12)
    birth_id2= models.CharField(max_length=12)
    adress1= models.CharField(max_length=30)
    adress2= models.CharField(max_length=30)
    
