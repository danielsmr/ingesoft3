from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import Login_Form, Consulta_nombre, Registro, Login_ven, Vendedor_form, Factura_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Producto, Cliente, Vendedor,Factura,articulo
from django.shortcuts import redirect
import json

def Lading(request):
	ctx = {}
	return render(request, "landing.html", ctx)

def Vendedor_log(request):
	login_form = Login_ven(request.POST or None)
	msg = ''
	if login_form.is_valid():
		form_data = login_form.cleaned_data
		username = form_data.get('Cedula')
		objects=""
		try:
			objects =Vendedor.objects.filter(Cedula=username)[0]
			aux=int(objects.Cedula)
			aux_user=int(username)
			if aux == aux_user :
				print("entro")
				return redirect("/Cajero")

			else:
				msg= "No existe el vendedor"
		except:
			msg= "No existe el vendedor"

			
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

	ctx = {
		"objects":objects,
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


def tem_regis(request):
	ctx={}
	objects = Producto.objects.all()
	ctx={'objects' : objects}
	return render (request,"registrar_articulos.html",ctx)

def regis_articulos(request, idProducto):

	Artic = articulo.objects.all()

	if len(Artic) == 0:
		prod= Producto.objects.get(idProducto = idProducto)
		articuloc = articulo.objects.create(idProducto = prod, Cantidad = "1")
	else:
		articuloc= articulo.objects.get(idProducto = idProducto)
		articuloc.Cantidad=str(int(articuloc.Cantidad)+1)
		articuloc.save()

	return redirect("/registro_v/" + str(articuloc.idarticulo))

	

def Registro_ventas(request, idarticulo):
	ctx = {}
	register_form = Factura_form(request.POST or None)

	if register_form.is_valid():
		
		print("entro")
		form_data = register_form.cleaned_data
		NumeroFactura = form_data.get("NumeroFactura")
		nitEmpresa = form_data.get("nitEmpresa")
		idCliente = form_data.get("idCliente")
		Nombre = form_data.get("Nombre")
		direccion = form_data.get("direccion")
		telefono = form_data.get("telefono")
		mediopago=form_data.get("mediopago")
		art = articulo.objects.get(idarticulo=idarticulo)
		
		
		total = int(art.Cantidad)*int(art.idProducto.Precio)


		cedula_v=Vendedor.objects.get(Cedula="1088341899")
		factura = Factura.objects.create(NumeroFactura=NumeroFactura,nitEmpresa=nitEmpresa,idCliente=idCliente,Nombre=Nombre,direccion=direccion,telefono=telefono,mediopago=mediopago,idarticulo= art,total=total,cedula_v=cedula_v)

		print("guardado")
		return redirect("/menu")
	else:
		print("salio")
	


	ctx = {
		'register_form' : register_form,
	}
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
	
	objects = Producto.objects.all()

	if register_form.is_valid() and request.method == 'POST':
		
		form_data = register_form.cleaned_data
		title = form_data.get("Nombre")
		objects =Producto.objects.filter(Nombre=title)
		print (title)
	

			
	ctx = {
		"objects":objects,
		
		'register_form': register_form
	}
	return render(request, "consulta.html", ctx)


def Sign_out(request):
	logout(request)
	return redirect("/")