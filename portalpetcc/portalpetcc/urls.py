"""portalpetcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403, handler404, handler500)

handler400 = 'portalpetcc.views.h404'
handler403 = 'portalpetcc.views.h404'
handler404 = 'portalpetcc.views.h404'
handler500 = 'portalpetcc.views.h500'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('home.urls')),
    url(r'^noticia/', include('noticia.urls')),
    url(r'^noticias/', 'noticia.views.ultimasnoticias'),
    url(r'^certificados/$', 'atividades.views.certificados'),
    url(r'^certificado/(?P<part_id>\d+)$', 'atividades.views.get_certificado'),
    url(r'^atividades/(?P<slug>[\w_-]+)$', 'projetos.views.atividades'),
    url(r'^sobre/$', 'home.views.sobre'),
    url(r'^minicursos/', include('atividades.urls')),
    url(r'^oportunidades/', include('oportunidades.urls')),
    url(r'^projetos/', include('projetos.urls')),
    url(r'^create_participacao/', 'atividades.views.createparticipacao'),
    url(r'^busca_certificados/', 'atividades.views.buscacertificados'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
