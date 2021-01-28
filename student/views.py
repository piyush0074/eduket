from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm as AF
from django.contrib.auth import authenticate, logout as user_logout
from django.contrib.auth import login as save_login

from .form import studentform
from .models import student

# Create your views here.


def stu_detail(request):
	print(request.user)
	if request.method == "POST":
		form = studentform(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			print(form)
			form.save()
			print("deatils saved")
			return redirect('/')
			
	form = studentform()
	args = {'form' : form}
	return render(request,'stu_detail.html',args)
	
	
