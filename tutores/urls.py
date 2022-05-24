# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import pagar_pedido, HistorialPedidosListView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='tutores.html'), name='tutores'),
    url(r'^denominaciones/crear/$', 'tutores.views.crear_denominacion', name='crear_denominacion'),
    url(r'^centros/crear/$', 'tutores.views.crear_centro', name='crear_centro'),
    url(r'^estudiantes/crear/$', 'tutores.views.crear_estudiante', name='crear_estudiante'),
    url(r'^calificaciones/crear/$', 'tutores.views.crear_calificacion', name='crear_calificacion'),
    url(r'^pedido/realizar/$', 'tutores.views.realizar_pedido', name='realizar_pedido'),
    #url(r'^factura/pagar/$', pagar_pedido.as_view(), name='pagar_pedido'),
    url(r'^factura/pagar/$', 'tutores.views.pagar_pedido', name='pagar_pedido'),
    url(r'^factura/pagar/(\d)/$', 'tutores.views.paga_pedido', name="paga_pedido"),
    #url(r'^pedido/realizar/$', PedidoCreateView.as_view(), name='realizar_pedido'),
    url(r'^pedidos/$', HistorialPedidosListView.as_view(), name="pedidos"),
    url(r'^pedidos/(\d)/$', 'tutores.views.pedido', name="pedido"),
    
)
