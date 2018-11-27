from django import forms
from .models import Producto, Cliente,Vendedor,Factura,Total,articulo

class Login_Form(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

class Login_ven(forms.Form):
	Cedula = forms.CharField(max_length=50) 
	class Meta:
		model = Vendedor
		fields = ['Cedula']

class Consulta_nombre(forms.Form):
	Nombre = forms.CharField(max_length=200)
	class Meta:
		model = Producto
		fields=['Nombre']
		
class Registro(forms.Form):
	idCliente = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	direccion = forms.CharField(max_length=50)
	email = forms.CharField(max_length=50)
	class Meta:
		model = Cliente
		fields=['idCliente', 'first_name', 'last_name', 'direccion', 'email']

class Vendedor_form(forms.Form):
	Cedula = forms.CharField(max_length=20)#segundos
	Nombre = forms.CharField(max_length=50)
	direccion = forms.CharField(max_length=20)#segundos
	telefono= forms.CharField(max_length=100)
	class Meta:
		model = Vendedor
		fields=['Cedula', 'Nombre', 'direccion', 'telefono']

class Factura_form(forms.Form):
	NumeroFactura = forms.CharField(max_length=20)#segundos
	nitEmpresa = forms.CharField(max_length=50)
	idCliente = forms.CharField(max_length=50)
	Nombre = forms.CharField(max_length=50)
	direccion= forms.CharField(max_length=50)
	telefono = forms.CharField(max_length=50)
	mediopago=forms.CharField(max_length=50)
	class meta:
		model= Factura
		fields =['NumeroFactura','nitEmpresa','idCliente','Nombre','direccion','telefono','mediopago']

