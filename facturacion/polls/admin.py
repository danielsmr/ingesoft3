from django.contrib import admin
from .models import Producto, Cliente,Vendedor,Factura,Total,articulo
# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Factura)
admin.site.register(Total)
admin.site.register(articulo)