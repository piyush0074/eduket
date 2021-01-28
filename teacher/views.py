from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .form import teacherform, uploadform, categoryform
from .models import teacher, notes, category
from student.models import student
from django.db.models import Exists
# Create your views here.

	
	
def teacher_detail(request):
	if request.method == "POST":
		form = teacherform(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			print(form)
			form.save()
			print("deatils saved")
			return redirect('/home/')
			
	form = teacherform()
	args = {'form' : form}
	return render(request,'teacher_detail.html',args)
	
def upload_doc(request):
	upload = True
	username = request.user
	if student.objects.filter(user=username).exists():
		upload = False
	if request.method == "POST":
		upload_file = request.FILES['doc']
		form = uploadform(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.doc = request.FILES['doc']
			form.user = request.user
			cat = form.branch
			if category.objects.filter(branch_name = cat):
				print("already added")
			else:
				br = category.objects.create(branch_name = cat)
				br.save()
				print("cat saved")
			form.save()
			return redirect('/home/')
	form = uploadform()
	args = {'upload':upload,'form':form}
	return render(request,'upload.html',args)
	
	
	
	
