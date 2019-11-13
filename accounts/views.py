from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
	if request.method == 'POST':
		# user has info n wanna create an account
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username']) 
				# check is an account already exists by this name
				return render(request,'accounts/signup.html',{'error':'User with this name already exists'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'accounts/signup.html',{'error':'Passwords did not match'})
	else:
		# user wants to enter info or many a times user is already signed in but just comes to this site
		# then he need not again provide all his details to visit the signup page 
		return render(request , 'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'accounts/login.html', {'error':'Oops ! Username or password is incorrect'})
	else:
		return render(request , 'accounts/login.html')


'''
	Logout better be a POST	request cuz some browsers like 'Chrome' automatically execute 'GET' req hence,
	user may automatically get logged out. To avaoid this keep POST req to logout page
'''
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
	