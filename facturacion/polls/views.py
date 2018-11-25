from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import Login_Form, Consulta_nombre, Registro, Login_ven, Vendedor_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Producto, Cliente, Vendedor
from django.shortcuts import redirect
import json

def Lading(request):
	ctx = {}
	return render(request, "landing.html", ctx)

def Vendedor_log(request):
	ctx = {}
	login_form = Login_ven(request.POST or None)
	msg = ''
	if login_form.is_valid():
		form_data = login_form.cleaned_data
		cedula = form_data.get('cedula')
		print (cedula)
		try:
			user = Vendedor.objects.get(Cedula=cedula)
		except Vendedor.DoesNotExist:
			user = None
		if user is not None:
			user = authenticate(Cedula=cedula)
			login(request, user)
			return redirect("/menu")
			
		else: 
			msg = 'No existe Usuario'

	ctx = {
		'login_form' : login_form,
		'msg' : msg,
	}
	return render(request, "index.html", ctx)

def menu_ad(request):
	ctx = {}
	return render (request, "menu.html", ctx)

def registar_vendedores(request):
	ctx={}

	register_form = Vendedor_form(request.POST or None)

	if register_form.is_valid():
		print("entro")
		form_data = register_form.cleaned_data

		Cedula = form_data.get("Cedula")
		
		Nombre = form_data.get("Nombre")
		print(Nombre)
		direccion = form_data.get("direccion")
		print(direccion)
		telefono = form_data.get("telefono")

		vendedor = Vendedor.objects.create(Cedula=Cedula, Nombre=Nombre,  direccion=direccion,  telefono=telefono)
		print("guardado")
		return redirect("/menu")





	objects = Vendedor.objects.all()

	for cont in objects:	
		
		objects_cedula=cont.Cedula
		objects_nombre=cont.Nombre
		objects_direccion=cont.direccion
		objects_telefono=cont.telefono
			
	ctx = {
		"objects":objects,
		"objects_cedula":objects_cedula,
		"objects_nombre":objects_nombre,
		"objects_direccion":objects_direccion,
		"objects_telefono":objects_telefono,
		'register_form': register_form
	}

	return render (request, "registrar_vendedores.html", ctx)

def Administrador(request):
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
				return redirect("/menu")
			else:
				msg = 'Contraseña incorrecta'
		else: 
			msg = 'No existe Usuario'

	ctx = {
		'login_form' : login_form,
		'msg' : msg,
	}

	return render(request, "admin.html", ctx)

def inicio(request):
	ctx = {}
	return render(request, "cajero.html", ctx)


def Registro_ventas(request):
	ctx = {}
	return render(request, "registro_v.html", ctx)


def Registro_clientes(request):
	ctx = {}
	register_form = Registro(request.POST or None)

	if register_form.is_valid():
		
		form_data = register_form.cleaned_data

		idCliente = form_data.get("idCliente")
		
		first_name = form_data.get("first_name")
		print(first_name)
		last_name = form_data.get("last_name")
		print(last_name)
		direccion = form_data.get("direccion")
		print(direccion)
		email = form_data.get("email")
		print(email)
		cliente = Cliente.objects.create(idCliente=idCliente, first_name=first_name, last_name=last_name, direccion=direccion,  email=email)
		print("guardado")
		return redirect("/Cajero")


	objects = Cliente.objects.all()

	for cont in objects:	
		objects_id=cont.idCliente
		objects_nombre=cont.first_name
		objects_snombre=cont.last_name
		objects_cantidad=cont.direccion
		objects_precio=cont.email
			
	ctx = {
		"objects":objects,
		"objects_id":objects_id,
		"objects_nombre":objects_nombre,
		"objects_snombre":objects_snombre,
		"objects_cantidad":objects_cantidad,
		"objects_precio":objects_precio,
		'register_form': register_form
	}




	return render(request, "registo_c.html", ctx)


def Consulta(request):
	register_form=Consulta_nombre(request.POST or None)
	
	if register_form.is_valid():
		
		print ("entro")
		form_data = register_form.cleaned_data
		title = form_data.get("titulo_Producto")
		print (title)


	objects = Producto.objects.all()

	for cont in objects:	
		objects_id=cont.idProducto
		objects_nombre=cont.Nombre
		objects_cantidad=cont.Cantidad
		objects_precio=cont.Precio
			
	ctx = {
		"objects":objects,
		"objects_id":objects_id,
		"objects_nombre":objects_nombre,
		"objects_cantidad":objects_cantidad,
		"objects_precio":objects_precio,
		'register_form': register_form
	}
	return render(request, "consulta.html", ctx)


def Sign_out(request):
	logout(request)
	return redirect("/")