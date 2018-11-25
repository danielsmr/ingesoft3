from django.db import models

# Create your models here.
class Producto(models.Model):
	class Meta:
		verbose_name = u"Producto"
		verbose_name_plural  = u"Productos"

	idProducto = models.CharField(max_length=20)#segundos
	Nombre = models.CharField(max_length=50)
	Cantidad = models.CharField(max_length=20)#segundos
	Precio= models.CharField(max_length=100)

class Vendedor(models.Model):
	class Meta:
		verbose_name = u"Vendedor"
		verbose_name_plural  = u"Vendedores"

	Cedula = models.CharField(max_length=20, unique=True)#segundos
	Nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=20)#segundos
	telefono= models.CharField(max_length=100)
	

class Cliente(models.Model):
	idCliente = models.CharField(primary_key=True, max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=50,unique=True)

	class Meta:
		verbose_name = u'Cliente'
		verbose_name_plural = u'Clientes'

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name


