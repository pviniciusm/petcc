from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.projetos),
    url(r'^ensino/', views.ensino),
    url(r'^extensao/', views.extensao),
    url(r'^pesquisa/', views.pesquisa),
]