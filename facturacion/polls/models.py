from django.db import models

# Create your models here.
class Producto(models.Model):
	class Meta:
		verbose_name = u"Producto"
		verbose_name_plural  = u"Productos"

	User = models.CharField(max_length=50)
	idProducto = models.CharField(max_length=20)#segundos
	Cantidad = models.CharField(max_length=20)#segundos
	Precio= models.CharField(max_length=100)
	