from django.db import models

# Create your models here.
class Producto(models.Model):
	class Meta:
		verbose_name = u"Producto"
		verbose_name_plural  = u"Productos"

	idProducto = models.CharField(primary_key=True, max_length=20)#segundos
	Nombre = models.CharField(max_length=50)
	Cantidad = models.CharField(max_length=20)#segundos
	Precio= models.CharField(max_length=100)

class Vendedor(models.Model):
	class Meta:
		verbose_name = u"Vendedor"
		verbose_name_plural  = u"Vendedores"

	Cedula = models.CharField( primary_key=True, max_length=20, unique=True)#segundos
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

class articulo(models.Model):
	
	idarticulo = models.CharField(primary_key=True, max_length=20)#segundos
	idProducto = models.ForeignKey('Producto',max_length=20,on_delete=models.CASCADE,)#segundos

	class meta:
		verbose_name= u'Articulo'
		verbose_name_plural=u'Articulos'

class Total(models.Model):
	idtotal = models.CharField(primary_key=True, max_length=50)
	subtotal= models.CharField(max_length=50)
	iva= models.CharField(max_length=50)
	total_t=models.CharField(max_length=50)

	class meta:
		"""docstring for meta"""
		verbose_name=u'Total'
		verbose_name_plural=u'Totales'			

class Factura(models.Model):
	NumeroFactura = models.CharField( primary_key=True, max_length=20, unique=True)#segundos
	nitEmpresa = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now_add=True)
	idCliente = models.CharField(max_length=50)
	Nombre = models.CharField(max_length=50)
	direccion= models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	idarticulo= models.ForeignKey('articulo', max_length=20,on_delete=models.CASCADE,)
	idtotal=models.ForeignKey('Total', max_length=50,on_delete=models.CASCADE,)
	mediopago=models.CharField(max_length=50)
	cedula_v=models.ForeignKey('Vendedor', max_length=50,on_delete=models.CASCADE,)
	
	class meta:
		verbose_name= u'Factura'
		verbose_name_plural=u'Facturas'







