from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username
