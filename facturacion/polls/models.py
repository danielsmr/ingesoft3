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
	