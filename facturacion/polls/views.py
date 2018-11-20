from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import Login_Form, Consulta_nombre
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Producto
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
	titulo_producto = Consulta_nombre(request.POST or None)
	objects = Producto.objects.all()
	if titulo_producto.is_valid():
		form_data_title = titulo_producto.cleaned_data
		title_name = form_data_title.get('titulo_producto')

		
		for cont in objects:
			if title_name == cont.Nombre :
				objects_id=cont.idProducto
				objects_nombre=cont.Nombre
				objects_cantidad=cont.Cantidad
				objects_precio=cont.Precio
			print ("no hay")
	else:
		objects_id='x'
		objects_nombre='x'
		objects_cantidad='x'
		objects_precio='x'

	ctx = {
		"objects":objects,
		"objects_id":objects_id,
		"objects_nombre":objects_nombre,
		"objects_cantidad":objects_cantidad,
		"objects_precio":objects_precio
	}
	return render(request, "consulta.html", ctx)


def Sign_out(request):
	logout(request)
	return redirect("/")