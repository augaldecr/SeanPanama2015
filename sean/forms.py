# -*- encoding: utf-8 -*-
from django import forms
from .models import Noticia, Mensaje, Comentario

class NoticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
		exclude = ['usuario_publicador']

class MensajeForm(forms.ModelForm):
	class Meta:
		model = Mensaje
		exclude = ['usuario_publicador']

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		exclude = ['comentador', 'fecha_comentario', 'aprobacion', 'noticia']