from django.contrib import admin
from .models import Oportunidade


# Register your models here.
class OportunidadeAdmin(admin.ModelAdmin):
    fields = ('titulo', 'texto', 'local', 'bolsa', 'carga', 'data_limite', 'edital',)
    list_display = ('titulo', 'local', 'bolsa', 'carga', 'usuario')

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.usuario = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Oportunidade, OportunidadeAdmin)