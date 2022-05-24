# -*- encoding: utf-8 -*-
from django.contrib import admin
from tutores.models import Calificacion, Centro, Denominacion, Distrito, Estudiante, Libro, Nivel, Provincia, Pedido, Fila_pedido, Factura

class CalificacionAdmin(admin.ModelAdmin):
	list_display = ('estudiante', 'nota', 'libro')
	list_display_links = ('estudiante',)
	list_editable = ('nota', 'libro')
	list_filter = ('estudiante', 'libro')
	ordering = ('estudiante',)
	search_fields = ('estudiante', 'libro')
	exclude =('usuario_publicador', )

class CentroAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'denominacion', 'distrito', 'ciudad', 'direccion',)
	list_display_links = ('nombre', 'denominacion', 'distrito',)
	list_editable = ('ciudad', 'direccion',)
	list_filter = ('nombre', 'denominacion', 'distrito', 'ciudad', 'direccion',)
	search_fields = ('nombre', 'denominacion', 'distrito', 'ciudad', 'direccion',)
	exclude =('usuario_publicador', )


class Fila_pedidoInline(admin.StackedInline):
	model = Fila_pedido
	extra = 1


class PedidoAdmin(admin.ModelAdmin):
	inlines = [Fila_pedidoInline]


class LibroAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'descripcion', 'imagen_portada')
	list_editable = ('nombre', 'descripcion',)

	def imagen_portada(self, obj):
		url = "/media/%s" % obj.portada
		tag = "<img height='160px' src='%s' width='120px'/>" % url
		return tag
	imagen_portada.allow_tags = True


class NivelAdmin(admin.ModelAdmin):
	list_display = ('nivel',)
	list_filter = ('nivel',)

	filter_horizontal = ('libros',)


admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Centro, CentroAdmin)
admin.site.register(Denominacion)
admin.site.register(Distrito)
admin.site.register(Estudiante)
admin.site.register(Factura)
admin.site.register(Libro, LibroAdmin)
#admin.site.register(Fila_pedido)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Provincia)