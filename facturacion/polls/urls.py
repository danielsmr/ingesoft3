from django.urls import path, re_path
from polls import views

urlpatterns = [
    path('', views.Lading, name="landing"),
    path('administrador', views.Administrador, name="Administrador"),
    path('vendedor', views.Vendedor_log, name="Vendedor"),
    path('Cajero', views.inicio, name="Inicio"),
    path('menu', views.menu_ad, name="Menu_ad"),
    path('registrar_vendedor', views.registar_vendedores, name="Registar_vendedores"),
    path('adios', views.Sign_out, name="Adios"),
    path('consulta', views.Consulta, name="Consulta"),
    path('registro_c', views.Registro_clientes, name="Registro_c"),
    path('registro_articulos/<idProducto>', views.regis_articulos, name="registro_articulos"),
    path('articulos',views.tem_regis, name="Articulo"),
    path('registro_v/<idarticulo>', views.Registro_ventas, name="Registro_v")
]
