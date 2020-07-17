from rest_framework import viewsets

from .serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
