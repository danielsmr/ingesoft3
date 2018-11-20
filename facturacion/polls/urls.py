from django.urls import path, re_path
from polls import views

urlpatterns = [
    path('', views.Lading, name="lading"),
    path('Cajero', views.inicio, name="Inicio"),
    path('adios', views.Sign_out, name="Adios")
]
