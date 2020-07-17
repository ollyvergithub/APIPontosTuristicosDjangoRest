from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # *** Autenticacao ***
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAdminUser,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (DjangoModelPermissions,)
    # authentication_classes = (TokenAuthentication, )

    # *** queryset substituido pelo  def get_queryset(self): ***
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # *** Habilitando o search field ***
    # *** Podemos escolher entre os lookups, colocando o simbolo na frente do campo ex ^endereco__linha1 ***
    # lookup_prefixes = {
    #         '^': 'istartswith',
    #         '=': 'iexact',
    #         '@': 'search',
    #         '$': 'iregex',
    #     }
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1'] # endereco__linha1 corresponde a uma ForeignKey em Endereco

    # *** Alterando o lookup padrao que é o id, mas tem que retornar apenas um registro ***
    # lookup_field = 'nome'

    def get_queryset(self):
        # Filtrando por query string
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.filter(aprovado=True)

        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            queryset.filter(nome__iexact=nome) # Ignorando case sensitive
        if descricao:
            queryset.filter(descricao__iexact=descricao) # Ignorando case sensitive

        # *** Ou podemos filtrar com Django Filters ***
        # filterset_fields = ['id', 'nome', 'descricao']
        return queryset

    # *** Sobrescrevendo as actions padrões do DjangoRest e Chamando os comportamentos padrões ***
    def list(self, request, *args, **kwargs): # Corresponde ao get
        # return Response({'teste': 123})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs): # Corresponde ao post
        # return Response({'Hello': request.data['nome']})
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs): # Corresponde ao delete
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs): # Recupera um id especifico, também disparado no get
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs): # Corresponde ao put
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs): # Corresponde ao patch, mas só para parte do objeto
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # *** Implementando nossas proprias actions personalizadas ***
    # *** Por exemplo Denunciar um ponto turístico ***
    @action(methods=['get'], detail=True) # detail=True indica que é para um registro e não para todo o endpoint
    def denunciar(self, request, pk=None):
        pass

    # *** Uma action para o nosso endpoint como um todo ***
    @action(methods=['post'], detail=False)
    def teste(self, request, pk=None):
        pass

    # *** Salvando uma aatracao com pontos turísticos já existentes no banco
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()

        return HttpResponse('OK')



