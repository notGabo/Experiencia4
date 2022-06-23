from django.urls import path
from rest_descuento.views import detalle_descuento, lista_descuento
urlpatterns = [
    path('lista_descuento',lista_descuento, name="lista_descuento"),
    path('detalle_descuento/<id>',detalle_descuento,name="detalle_descuento")
]