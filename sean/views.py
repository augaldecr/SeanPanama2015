# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 

from sean.models import Noticia, Comentario
from sean.forms import NoticiaForm, MensajeForm, ComentarioForm
from tutores.models import Libro, Nivel

def noticias(request):
	noticias = Noticia.objects.order_by("-fecha_publicacion").all()
	return render(request,"noticias.html", {"noticias":noticias})

def noticia(request, pk):
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid:
			msg = "Su comentario fué enviado y está a la espera de aprobación"
			comentario = form.save( commit=False )
			comentario.comentador = request.user
			noticia = get_object_or_404(Noticia, pk=pk)
			comentario.noticia = noticia
			comentario.save()
			#return HttpResponseRedirect(reverse("noticia_msg", args={id, mensaje}))
			return redirect("/noticias/%s/"%pk)
	else:
		form = ComentarioForm()
		noticia = get_object_or_404(Noticia,pk=pk)
		form = ComentarioForm()
	return render(request,"noticia.html", {"noticia":noticia, 'form':form})

def comentario(request, id):
	noticia = get_object_or_404(Noticia,pk=id)
	return render(request,"noticia.html", {"noticia":noticia})

def libros(request):
	niveles = Nivel.objects.order_by("pk").all()
	return render(request,"libros.html", {"niveles":niveles})

def libro(request, id):
	libro = get_object_or_404(Libro,pk=id)
	return render(request,"libro.html", {"libro":libro})

@login_required
def crear_noticia(request):
	if request.method == 'POST':
		form = NoticiaForm(request.POST)
		if form.is_valid:
			noticia = form.save( commit=False )
			noticia.usuario_publicador = request.user
			noticia.save()
			return redirect("home")
	else:
		form = NoticiaForm()
	return render(request,"form.html", {'form':form,"titulo":"Crear noticia"})

def crear_mensaje(request):
	if request.method == "POST":
		form = MensajeForm(request.POST)
		if form.is_valid:
			mensaje = form.save( commit=False )
			mensaje.usuario_publicador = request.user
			mensaje.save()
			return redirect('home')
	else:
		form = MensajeForm()
	return render(request, "form.html", {"form":form,"titulo":"Contáctenos"})