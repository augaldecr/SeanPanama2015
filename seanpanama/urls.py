from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from .settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('sean.urls')),
    url(r'^tutores/', include('tutores.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
)
