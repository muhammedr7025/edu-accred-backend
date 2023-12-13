from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
  USERNAME_FIELD = "email"
  first_name = models.CharField(max_length=200,null=False,blank=False)
  last_name = models.CharField(max_length=100,null=False,blank=False)
  email = models.EmailField(unique=True,null=False,blank=False)
  user_role = models.CharField(max_length=100,null=False,blank=False)
  REQUIRED_FIELDS = ('first_name','last_name','password','user_role')

class Department(models.Model):
    id = models.CharField(primary_key=True,max_length=100,null=False,blank=False,default=uuid.uuid4)
    name = models.CharField(max_length=100,null=False,blank=False,unique=True)
    hod = models.ForeignKey(CustomUser,on_delete=models.CASCADE,unique=True)

class Student(models.Model):
    id = models.CharField(primary_key=True,max_length=100,null=False,blank=False,default=uuid.uuid4)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,unique=True)
    batch = models.CharField(max_length=100,null=False,blank=False,unique=True)

class Staff(models.Model):
    id = models.CharField(primary_key=True,max_length=100,null=False,blank=False,default=uuid.uuid4)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,unique=True)
    department = models.CharField(max_length=100,null=False,blank=False)

admin.site.register(Student)
admin.site.register(CustomUser)