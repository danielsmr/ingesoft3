from django.urls import path, re_path
from polls import views

urlpatterns = [
    path('', views.Lading, name="Lading"),
    path('Cajero', views.inicio, name="Inicio"),
    path('adios', views.Sign_out, name="Adios"),
    path('consulta', views.Consulta, name="Consulta"),
    path('registro_c', views.Registro_clientes, name="Registro_c")
]
