from django.db import models


class Server(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
