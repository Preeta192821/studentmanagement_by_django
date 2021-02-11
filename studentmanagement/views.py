from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from django.core.cache import cache
from django.contrib import messages
from .models import user

# Create your views here.mplat

def loginRequired(methodName):
	def wrapper(*args,**keywords):
		request = args[0]
		if 'username_key' in request.session:
			return methodName(*args,**keywords)
		else:
			return redirect(login)
	return wrapper

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confpassword=request.POST['conf_password']
		email = request.POST['email']
		if password==confpassword:
			u = user.registerUser(username,email,password)
			if isinstance(u,user):
				message = '{0} registered'.format(username)
				return redirect(login)

			elif u == -1:
				messages.info(request,'User Already Exists')
				return render(request,'register.html')
			else:
				print(u)
				messages.info(request,'Unexpected error occured')
				return render(request,'register.html')
		else:
			messages.info(request,"Passwords Don't Match")
			return render(request,'register.html')

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	elif request.method == 'POST':
		email= request.POST['email']
		password = request.POST['password']
		u = user.loginUser(email,password)
		if isinstance(u,user):
			#request.session['username_key'] = u.username
			request.session['username_key'] = email
			return redirect(login)
			#want to send username
			#return render(request, 'index.html',{'message':message})
		elif u == -1:
			messages.info(request,'Username or password is invalid')
			return render(request,'login.html')
		else:
			messages.info(request,'Unexpected error occured')
			return render(request,'login.html')



def Home(request):
	return render(request,'home.html')



def About(request):
	return render(request,'about.html')



def Contact(request):
	return render(request,'contact.html')


def logout(request):
	del request.session['username_key']
	cache.clear()
	return redirect(login)


def Gallery(request):
	return render(request,'gallery.html')
































































































































































# Create your views here.
