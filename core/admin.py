from django.contrib import admin
from .models import Persona, Project

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo_electronico', 'telefono', 'titulo_academico')
    search_fields = ('nombres', 'apellidos', 'correo_electronico')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created', 'updated')