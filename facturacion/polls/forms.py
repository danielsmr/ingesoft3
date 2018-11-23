from django import forms
from .models import Producto, Cliente

class Login_Form(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

class Consulta_nombre(forms.Form):
	titulo_Producto = forms.CharField(max_length=200)
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