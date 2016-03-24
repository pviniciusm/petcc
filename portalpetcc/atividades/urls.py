from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.minicursos),
    url(r'^antigos/', views.minicursos_antigos),
]