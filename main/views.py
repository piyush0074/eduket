from django.http import HttpResponse, Http404, FileResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm as AF
from django.contrib.auth import authenticate, logout as user_logout
from django.contrib.auth import login as save_login
from student.models import student
from student.form import signin_form
from teacher.models import teacher, notes, category
from django.db.models import Q
from django_mfa.models import is_u2f_enabled

# Create your views here.
def home(request):
	upload = True
	username = request.user
	cat = category.objects.all()
	if student.objects.filter(user=username).exists():
		upload = False
	document = reversed(notes.objects.all())
	args = {'document':document, 'upload':upload,'cat':cat}
	return render(request,"home.html",args)

def about(request):
	return render(request=request,template_name="aboutus.html")
	
def middle(request):
	return render(request,'middle.html')
	
	
	
def login(request):
	if request.method == "POST" :
		form = AF(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			username  = authenticate(username=username,password=password)
			stu = student.objects.filter(user=username)
			if student.objects.filter(user=username).exists() or teacher.objects.filter(user=username).exists() :
				if username is not None:
					save_login(request,username)
					return redirect('/home/')
			else:
				save_login(request,username)
				return redirect('/middle/')
			'''if username is not None:
					save_login(request,username)
					return redirect('/stu_detail/')'''
	form = AF()
	args = {'form' : form}
	return render(request,'login.html',args)
	


def signin(request):
	if request.method == "POST":
		form = signin_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			return redirect('/login/')
	else:
		form = signin_form()
	args = {'form' : form}
	return render(request,'signin.html',args)
	
def logout(request):
	user_logout(request)
	return redirect('/login/')
	
	
def profile(request):
	upload = True
	username = request.user
	if student.objects.filter(user=username).exists():
		upload = False
	args = {'upload':upload}	
	if teacher.objects.filter(user=username).exists():
		documents = notes.objects.filter(user=username).reverse()
		detail = reversed(teacher.objects.filter(user=username))
		args.update({'documents':documents,'detail':detail})
	return render(request,'profile.html',args)

def delete(request):
	noteid = int(request.GET.get('id'))
	uid = request.user.id
	document = notes.objects.get(note_id=noteid)
	br = document.branch
	print(br)
	document.delete()
	return redirect('/profile/')
	
	
def account(request):
	upload  = True
	username = request.user
	if student.objects.filter(user=username).exists():
		upload = False
	args = {'upload':upload}
	return render(request,'account.html',args)
	
	
def search(request):
	upload = True
	username = request.user
	if student.objects.filter(user=username).exists():
		upload = False
	args = {'upload':upload}
	if request.method == "GET":
		query = request.GET.get('q')
		submitbutton = request.GET.get('submit')
		if query is not None:
			subject = notes.objects.filter(subject_name = query)
			br = notes.objects.filter(branch = query)
			#name = notes.objects.filter(user = query)
			args.update({'subject':subject,'br':br})
			print(args)
	return render(request,'search.html',args)	



def cate_show(request):
	cat = request.GET.get('q')
	upload = True
	username = request.user
	if student.objects.filter(user=username).exists():
		upload = False
	result = notes.objects.filter(branch=cat)
	print(result)
	args = {'upload':upload,'result':result}
	return render(request,'category.html',args)
	
	
def pdf_view(request):
	root = "media/"
	filename = root + request.GET.get('view')
	try:
		print(filename)
		return FileResponse(open(filename, 'rb'), content_type='application/pdf')
	except FileNotFoundError:
		print("no")
		raise Http404()









	
