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

class HealthCheck(models.Model):
    class Status(models.TextChoices):
        UP = "UP", "UP"
        DOWN = "DOWN", "DOWN"
        TIMEOUT = "TIMEOUT", "Timeout"
        UNKNOWN = "UNKNOWN", "Unknown"

    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="health_checks",
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.UNKNOWN,
    )

    response_time = models.PositiveIntegerField()
    checked_at = models.DateTimeField(auto_now_add=True)