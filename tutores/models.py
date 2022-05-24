# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.TextField(max_length=350)
    portada = models.ImageField(upload_to='portadas')
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    nivel = models.CharField(max_length=35)
    libros = models.ManyToManyField('Libro')
    
    def __str__(self):
        return self.nivel

class Provincia(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Distrito(models.Model):
    nombre = models.CharField(max_length=30)
    provincia = models.ForeignKey('Provincia')
    
    def __str__(self):
        return self.nombre

class Denominacion(models.Model):
    nombre = models.CharField(max_length=140)
    usuario_publicador = models.ForeignKey(User)
    
    def __str__(self):
        return self.nombre

class Centro(models.Model):
    nombre = models.CharField(max_length=140)
    denominacion = models.ForeignKey('Denominacion')
    distrito = models.ForeignKey('Distrito')
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=140)
    usuario_publicador = models.ForeignKey(User)
    
    def __str__(self):
        return u" %s - %s - %s " %(self.nombre, self.denominacion, self.ciudad)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField()
    centro = models.ForeignKey('Centro')
    usuario_publicador = models.ForeignKey(User)
    
    def __str__(self):
        return u" %s %s - %s " %(self.nombre, self.apellido, self.centro)
    
class Calificacion(models.Model):
    estudiante = models.ForeignKey('Estudiante')
    nota = models.FloatField()
    libro = models.ForeignKey('Libro')
    tutor = models.ForeignKey(User)
    
    def __str__(self):
        return u" %s - %s - %s - %s " %(self.estudiante, self.nota, self.libro, self.tutor)

class Fila_pedido(models.Model):
    cantidad = models.PositiveSmallIntegerField()
    libro = models.ForeignKey('Libro')
    pedido = models.ForeignKey('Pedido')

    def suma(self):
        return self.cantidad * self.libro

    def __str__(self):
        return "Línea de pedido"

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(User)
    facturado = models.BooleanField(default=False)
    total = models.FloatField()
    
    def __str__(self):
        return u"%s - %s"%(self.fecha, self.tutor)

class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    numero_recibo = models.CharField("Numero de recibo", max_length=15)
    recibo_img = models.ImageField("Recibo escaneado", upload_to='recibos', blank=True)
    pedido = models.OneToOneField('Pedido')
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return u"%s - %s"%(self.fecha, self.pedido.tutor)