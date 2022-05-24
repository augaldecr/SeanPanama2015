# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^noticias/$', 'sean.views.noticias', name='noticias'),
    url(r'^noticias/(\d)/$', 'sean.views.noticia', name="noticia"),
    url(r'^cursos/$', 'sean.views.libros', name='cursos'),
    url(r'^cursos/(\d)/$', 'sean.views.libro', name="curso"),
    url(r'^historia/$', TemplateView.as_view(template_name='historia.html'), name='historia'),
    url(r'^noticias/crear/$', 'sean.views.crear_noticia', name='crear_noticia'),
    url(r'^contactenos/$', 'sean.views.crear_mensaje', name='crear_mensaje'),
)
