# -*- encoding: utf-8 -*-

from random import choice
from django.core.urlresolvers import reverse
from sean.models import Noticia

versiculos = ('Jesús dijo: Yo soy el camino, la verdad y la vida',)

def versiculo(request):
	return {'versiculo' : choice(versiculos)}

def menu(request):
	menu = {'menu': [
		{'name': 'Inicio', 'url': reverse('home'), 'clase': 'icon-home-outline' },
		{'name': 'Noticias', 'url': reverse('noticias'),'clase': 'icon-news'},
        {'name': 'Cursos', 'url': reverse('cursos'), 'clase': 'icon-doc-text'},
		{'name': 'Historia', 'url': reverse('historia'), 'clase': 'icon-globe-alt-outline'},
		{'name': 'Contáctenos', 'url': reverse('crear_mensaje'), 'clase': 'icon-mail'},
	]}
	for item in menu['menu']:
		if request.path == item["url"]:
			item["active"] = True
	return menu

def ultimas_noticias(request):
	ultimas_noticias = Noticia.objects.order_by("-fecha_publicacion").all()[:3]
	return {'ultimas_noticias':ultimas_noticias}