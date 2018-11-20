from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import Login_Form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

def Lading(request):
	login_form = Login_Form(request.POST or None)
	msg = ''
	if login_form.is_valid():
		form_data = login_form.cleaned_data
		username = form_data.get('username')
		password = form_data.get('password')
		print (username)
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		if user is not None:
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("/Cajero")
			else:
				msg = 'Contraseña incorrecta'
		else: 
			msg = 'No existe Usuario'

	ctx = {
		'login_form' : login_form,
		'msg' : msg,
	}
	return render(request, "index.html", ctx)

def inicio(request):
	ctx = {}
	return render(request, "cajero.html", ctx)

def Consulta(request):
	ctx = {}
	return render(request, "consulta.html", ctx)


def Sign_out(request):
	logout(request)
	return redirect("/")