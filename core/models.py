from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    titulo_academico = models.CharField(max_length=100, verbose_name="Título académico")
    biografia = models.TextField(verbose_name="Biografía")
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    dedicacion = models.CharField(max_length=100, verbose_name="Dedicación Persona")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen", null=True, blank=True)
    link = models.URLField(max_length=200, verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title