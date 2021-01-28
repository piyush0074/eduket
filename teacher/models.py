from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now
from django.utils import timezone

#from phonenumber_field.formfields import PhoneNumberField

# Create your models here.

class teacher(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20,null=False)
	last_name = models.CharField(max_length=20,null=False)
	phone_no = models.CharField(primary_key=True,max_length=15)
	college_name = models.CharField(max_length=40,null=False)
	designation = models.CharField(max_length=20,null=False)
	
	
	
class notes(models.Model):
	note_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	doc = models.FileField(upload_to='documents/')
	branch = models.CharField(max_length=50,null=False,default='NA')
	subject_name = models.CharField(max_length=50,null=False)
	uploaded_time = models.TimeField(("Time"),default=now)
	uploaded_date = models.DateField(("Date"),default=datetime.date.today)
	
	
	
class category(models.Model):
	branch_name = models.CharField(max_length=50,null=False,default='NA')
	
