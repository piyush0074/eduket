from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import teacher, notes, category
#from phonenumber_field.formfields import PhoneNumberField




class teacherform(ModelForm):
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	phone_no = forms.CharField(max_length=15)
	college_name = forms.CharField(max_length=40)
	designation = forms.CharField(max_length=20)

	class Meta:
		model = teacher
		fields = ('first_name','last_name','phone_no','college_name','designation')
		
		
class uploadform(ModelForm):
	subject_name = forms.CharField(max_length=50)
	branch = forms.CharField(max_length=50)
	doc = forms.FileField(label='Select a file', help_text='max size 20mb')	
	
	class Meta:
		model = notes
		fields = ('subject_name','branch','doc')	
	
	
class categoryform(ModelForm):

	class Meta:
		model = category
		fields = ('branch_name',)	
	
	
	
