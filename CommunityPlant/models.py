from tabnanny import verbose
from django.db import models

class Usuarios(models.Model):
    username = models.CharField(max_length=30,primary_key=True, verbose_name='Nombre de usuario')
    mail = models.CharField(max_length=60, null=False, blank=False,unique=True, verbose_name='Correo')
    password = models.CharField(max_length=60, null=False, blank=False, verbose_name='Contraseña')
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.username
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        del self

class FormSolicitud(models.Model):
    idSolicitud = models.AutoField(primary_key=True, verbose_name='Id solicitud')
    nombreCompleto = models.CharField(max_length=60, null=False, verbose_name='Nombre completo')
    mailSolicitante = models.CharField(max_length=60, null=False, verbose_name='Mail del solicitate')
    descripcion = models.CharField(max_length=1000, null=False, verbose_name='Descripcion')
    class Meta:
        verbose_name_plural = 'FormSolicitud'
    def __str__(self):
        return self.nombreCompleto

class CategoriaPlanta(models.Model):
    idCategoria = models.IntegerField(primary_key=True,null=False, blank=False, verbose_name='Id categoria')
    nombreCategoria = models.CharField(max_length=40 ,unique=True, null=False, blank=False, verbose_name='Nombre categoria')
    class Meta:
        verbose_name_plural = 'CategoriaPlanta'
        def __str__(self):
            return self.nombreCategoria

class CatalogoPlantas(models.Model):
    idPlanta = models.AutoField(primary_key=True, verbose_name='Id planta')
    nombrePlanta = models.CharField(max_length=30, null=False, blank=False, unique=True, verbose_name='Nombre planta')
    descripcionPlanta = models.CharField(max_length=500, null=False, blank=True, verbose_name='Descripcion planta')
    precioPlanta  = models.IntegerField(null=False,blank=False, verbose_name='Precio planta')
    categoria =  models.ForeignKey(CategoriaPlanta, on_delete=models.CASCADE)
    imagenPlanta = models.CharField(max_length=2000, verbose_name='url foto planta')   
    stockPlanta = models.IntegerField(null=False, blank=False, verbose_name='Stock planta')
    class Meta:
        verbose_name_plural = 'CatalogoPlantas'
    def __str__(self):
        return self.nombrePlanta

class boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True, verbose_name='Numero boleta')
    precioTotal = models.IntegerField(null=False, blank=False, verbose_name='Precio total')
    fecha = models.DateField(verbose_name='Fecha boleta')

    def __str__(self):
        return str(self.idBoleta)

## Create your models here.

