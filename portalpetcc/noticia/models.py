from django.db import models
from datetime import datetime
from home.models import User
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
import os


def get_img_path(instance, filename):
    return os.path.join('image/noticia', 'noticia'+filename)


# Create your models here.
class Noticia(models.Model):
    data = models.DateTimeField(
            default=datetime.now,
            blank=True
    )
    usuario = models.ForeignKey(User, blank=True)
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image = models.ImageField(blank=True, upload_to=get_img_path)
    vertical = models.BooleanField(blank=True, default=False, help_text="Opção para marcar quando a imagem da notícia for muito alta, para que não fique mal exibida")
    visualizacoes = models.IntegerField(editable=False, auto_created=True, default=0)

    def __unicode__(self):
        return "%s" % self.id

    def get_absolute_url(self):
        return reverse(
            'noticia.views.noticias',
            kwargs={'slug':self.slug}
        )


def noticia_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0

        while Noticia.objects.filter(
            slug = novo_slug
        ).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug


signals.pre_save.connect(noticia_pre_save, sender=Noticia)
