from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
User.add_to_class('bday', models.DateField(default=datetime.now))
User.add_to_class('participante', models.BooleanField(blank=True, default=False))
User.add_to_class('matricula', models.CharField(max_length=100, blank=True, unique=True))
User.add_to_class('curso', models.CharField(max_length=100, blank=True, default="Ciencia da Computacao"))


class Aluno(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='first name', blank=True)
    last_name = models.CharField(max_length=50, verbose_name='last name', blank=True)
    email = models.EmailField(max_length=254, verbose_name='email address', blank=True)
    username = models.CharField(max_length=30, verbose_name='username', unique=True, blank=True)

    participante = models.BooleanField(blank=True, default=False)
    matricula = models.CharField(max_length=100, blank=True, unique=True)
    curso = models.CharField(max_length=100, blank=True, default="Ciencia da Computacao")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
