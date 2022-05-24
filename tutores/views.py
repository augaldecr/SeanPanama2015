# -*- encoding: utf-8 -*-

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView

from .models import Pedido, Fila_pedido
from .forms import DenominacionForm, CentroForm, EstudianteForm, CalificacionForm, PedidoForm, Fila_pedidoFormSet, FacturaForm

@login_required
def home(request):
    pass

@login_required
def crear_denominacion(request):
    titulo = "Ingreso de denominación"
    if request.method == "POST":
        form = DenominacionForm(request.POST)
        if form.is_valid:
            denominacion = form.save( commit=False )
            denominacion.usuario_publicador = request.user
            denominacion.save()
            return redirect("crear_denominacion")
    else:
        form = DenominacionForm()
    return render(request, "form_tutores.html", {"form":form, "titulo":titulo})

@login_required
def crear_centro(request):
    titulo = "Ingreso de centro de estudio"
    if request.method == "POST":
        form = CentroForm(request.POST)
        if form.is_valid:
            centro = form.save( commit=False )
            centro.usuario_publicador = request.user
            centro.save()
            return redirect('crear_centro')
    else:
        form = CentroForm()
    return render(request, "form_tutores.html", {"form":form, "titulo":titulo})

@login_required
def crear_estudiante(request):
    titulo = "Ingreso de estudiante al sistema"
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid:
            estudiante = form.save( commit=False )
            estudiante.tutor = request.user
            estudiante.save()
            return redirect('crear_estudiante')
    else:
        form = EstudianteForm()
    return render(request, "form_tutores.html", {"form":form, "titulo":titulo})

@login_required
def crear_calificacion(request):
    titulo = "Ingreso de calificación de estudiante"
    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid:
            calificacion = form.save( commit=False )
            calificacion.usuario_publicador = request.user
            calificacion.save()
            return redirect('crear_calificacion')
    else:
        form = CalificacionForm()
    return render(request, "form_tutores.html", {"form":form, "titulo":titulo})

@login_required
def realizar_pedido(request):
    if request.POST:
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.tutor = request.user
            fila_pedido_formset = Fila_pedidoFormSet(request.POST, instance=pedido)
            if fila_pedido_formset.is_valid():
                pedido.save()
                fila_pedido_formset.save()
                return HttpResponseRedirect(reverse('realizar_pedido'))
    else:
        form = PedidoForm()
        fila_pedido_formset = Fila_pedidoFormSet(instance=Pedido())
    return render_to_response("form_pedido.html", {
        "form": form,
        "fila_pedido_formset": fila_pedido_formset,
    }, context_instance=RequestContext(request))

@login_required
def pagar_pedido(request):
    pedidos = Pedido.objects.order_by("-fecha").filter(tutor=request.user).filter(facturado=False)
    return render(request,"list_pedidos.html", {"pedidos":pedidos})

@login_required
def paga_pedido(request, pk):
    titulo = "Ingreso de calificación de estudiante"
    if request.POST:
        form = FacturaForm(request.POST)
        if form.is_valid():
            msg = "Su pago fué enviado y está a la espera de aprobación"
            factura = form.save( commit=False )
            #pedido = get_object_or_404(Pedido, pk=pk)
            pedido = Pedido.objects.get(pk=pk)
            pedido.facturado = True
            pedido.save()
            factura.pedido = pedido
            factura.save()
            #return HttpResponseRedirect(reverse("noticia_msg", args={id, mensaje}))
            return HttpResponseRedirect(reverse('pagar_pedido'))
    else:
        #factura = get_object_or_404(Pedido,pk=pk)
        form = FacturaForm()
    return render(request,"form_tutores.html", {'form':form, 'titulo':titulo})


class HistorialPedidosListView(ListView):
    model = Pedido
    template_name = "pedidos_list.html"

    def get_queryset(self, **kwargs):
        query = Pedido.objects.filter(facturado=True)
        return query

@login_required
def pedido(request, pk):
    pedido = Pedido.objects.filter(tutor=request.user).get(pk=pk)
    fila_pedido = Fila_pedido.objects.filter(pedido=pk)
    return render(request,"pedido.html", {"pedido":pedido, "fila_pedido":fila_pedido})