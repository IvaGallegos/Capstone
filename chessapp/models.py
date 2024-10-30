# models.py
from django.db import models
from django.contrib.auth.models import User

class Partida(models.Model):
    jugador = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo de usuario
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la partida
    resultado = models.CharField(max_length=10)  # Resultado: 'Victoria', 'Derrota', 'Empate'
    movimientos = models.TextField()  # Registro de movimientos en formato PGN o similar

    def __str__(self):
        return f"{self.jugador.username} - {self.resultado} en {self.fecha}"


# Create your models here.
