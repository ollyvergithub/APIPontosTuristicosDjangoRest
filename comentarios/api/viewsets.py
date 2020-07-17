from rest_framework import viewsets

from .serializers import ComentarioSerializer
from comentarios.models import Comentario


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
