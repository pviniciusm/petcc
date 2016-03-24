from django.contrib import admin
from .models import Aluno
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#from django import forms
#from django.contrib.auth.forms import UserCreationForm




class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'id',)
    pass

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'matricula', 'email',)
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Aluno, AlunoAdmin)
