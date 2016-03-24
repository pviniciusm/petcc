from django.contrib import admin
from noticia.models import Noticia
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class NoticiaAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'slug', 'visualizacoes',)
    fields = ('data', 'titulo', 'conteudo', 'image', 'vertical',)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.usuario = user
        instance.save()
        form.save_m2m()
        return instance

    pass

admin.site.register(Noticia, NoticiaAdmin)


