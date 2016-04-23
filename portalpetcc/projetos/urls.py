from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.projetos),
    url(r'(?P<id>\d+)/$', views.projeto),
    url(r'^ensino/', views.ensino),
    url(r'^pesquisa/', views.pesquisa),
    url(r'^extensao/', views.extensao),
]
