from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.usuario.username


