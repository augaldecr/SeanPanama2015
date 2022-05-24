# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Noticia(models.Model):
    titulo = models.CharField(max_length=140)
    contenido = models.TextField(max_length=300)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    usuario_publicador = models.ForeignKey(User)
    
    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    contenido = models.TextField(max_length=140)
    comentador = models.CharField(max_length=45)
    comentador_email = models.EmailField()
    noticia = models.ForeignKey(Noticia)
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    aprobacion = models.BooleanField(default=False)
    
    def __str__(self):
        return self.contenido
    
#class Libro(models.Model):
#    nombre = models.CharField(max_length=70)
#    descripcion = models.TextField(max_length=350)
#    portada = models.ImageField(upload_to='portadas')
        
#    def __str__(self):
#        return self.nombre
    

# class Nivel(models.Model):
#     nivel = models.CharField(max_length=35)
#     libros = models.ManyToManyField('Libro')
    
#     def __str__(self):
#         return self.nivel
    
    
class Mensaje(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    mensaje = models.TextField(max_length=300)
    timestamp = models.DateTimeField("Fecha", auto_now_add=True)
    usuario_publicador = models.ForeignKey(User)
    
    def __str__(self):
        return self.nombre + " - " +self.email