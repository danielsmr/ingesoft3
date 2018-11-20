from django import forms

class Login_Form(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

class Consulta_nombre(forms.Form):
	titulo_Producto = forms.CharField(max_length=200)