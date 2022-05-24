# -*- encoding: utf-8 -*-
from django import forms
from .models import Calificacion, Centro, Denominacion, Estudiante, Libro, Pedido, Fila_pedido, Factura
from django.forms.models import inlineformset_factory


class DenominacionForm(forms.ModelForm):
	class Meta:
		model = Denominacion
		exclude = ['usuario_publicador']


class CentroForm(forms.ModelForm):
	class Meta:
		model = Centro
		exclude = ['usuario_publicador']


class EstudianteForm(forms.ModelForm):
	class  Meta:
		model = Estudiante
		exclude = ['usuario_publicador']


class CalificacionForm(forms.ModelForm):
	class Meta():
		model = Calificacion
		exclude = ['tutor']


class Fila_pedidoForm(forms.ModelForm):
    class Meta:
        model = Fila_pedido

    
class PedidoForm(forms.ModelForm):
 	class Meta:
 		model = Pedido
 		exclude = ['fecha', 'tutor', 'facturado']


Fila_pedidoFormSet = inlineformset_factory(Pedido,
    Fila_pedido,
    can_delete=True,
    extra=1)


class FacturaForm(forms.ModelForm):
 	class  Meta:
 		model = Factura
 		exclude = ['fecha', 'enviado']