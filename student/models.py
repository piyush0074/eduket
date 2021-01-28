from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.formfields import PhoneNumberField

# Create your models here.

class student(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=15,null=False)
	last_name = models.CharField(max_length=15,null=False)
	phone_no = models.CharField(primary_key=True,max_length=15)
	college_name = models.CharField(max_length=40,null=False)
	degree = models.CharField(max_length=10,null=False)
