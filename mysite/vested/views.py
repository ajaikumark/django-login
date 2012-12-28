from django.shortcuts import render_to_response
from django.template import RequestContext
from vested.models import Userdata
def register(request):
	return render_to_response("register.html",{"msg":''},context_instance=RequestContext(request))

def register_action(request):
	try:
		user = Userdata()
		user.username = request.POST['username']
		user.password = request.POST['password']
		user.save()
	except:
		msg="User registration failed"
	else:
		msg='User registerd successfully'
	return render_to_response("register.html",{'msg':msg},context_instance=RequestContext(request))

def login(request):
	return render_to_response("login.html",{},context_instance=RequestContext(request))

def login_action(request):
	return render_to_response("login_action.html",{},context_instance=RequestContext(request))	