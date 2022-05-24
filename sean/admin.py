# -*- encoding: utf-8 -*-
from django.contrib import admin
from sean.models import Noticia, Mensaje, Comentario

class ComentarioInline(admin.StackedInline):
	model = Comentario
	extra = 1

class NoticiaAdmin(admin.ModelAdmin):
	inlines = [ComentarioInline]
	list_display = ('id','titulo', 'contenido', 'fecha_publicacion', 'usuario_publicador')
	list_editable = ('titulo', 'contenido', 'usuario_publicador')
	list_filter = ('fecha_publicacion', 'usuario_publicador')
	search_fields = ('titulo', 'contenido')

# class LibroAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre', 'descripcion', 'imagen_portada')
# 	list_editable = ('nombre', 'descripcion',)

# 	def imagen_portada(self, obj):
# 		url = "/media/%s" % obj.portada
# 		tag = "<img height='160px' src='%s' width='120px'/>" % url
# 		return tag
# 	imagen_portada.allow_tags = True

# class NivelAdmin(admin.ModelAdmin):
# 	list_display = ('nivel',)
# 	list_filter = ('nivel',)

# 	filter_horizontal = ('libros',)

class MensajeAdmin(admin.ModelAdmin):
	list_display =('nombre', 'email', 'mensaje', 'timestamp', 'usuario_publicador')
	list_filter =('nombre', 'email', 'timestamp', 'usuario_publicador')
	search_fields = ('nombre', 'mensaje')

#admin.site.register(Libro, LibroAdmin)
admin.site.register(Mensaje, MensajeAdmin)
#admin.site.register(Nivel, NivelAdmin)
admin.site.register(Noticia, NoticiaAdmin)