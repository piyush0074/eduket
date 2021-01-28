from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import student
#from phonenumber_field.formfields import PhoneNumberField


class signin_form(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username','email','password1','password2')
	
	def save(self,commit=True):
		user = super(signin_form,self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

class studentform(ModelForm):
	first_name = forms.CharField(max_length=15)
	last_name = forms.CharField(max_length=15)
	phone_no = forms.CharField(max_length=15)
	college_name = forms.CharField(max_length=40)
	degree = forms.CharField(max_length=10)

	class Meta:
		model = student
		fields = ('first_name','last_name','phone_no','college_name','degree')
		
	
	
	
	
