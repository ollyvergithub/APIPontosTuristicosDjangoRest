from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, Atracao, Endereco, DocIdentificacao, Avaliacao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = "__all__"

class PontoTuristicoSerializer(ModelSerializer):
    # *** Nested relationships - Traz todos os campos do models relacionados ***
    # *** O parâmetro read_only=True serve para incluirmos via post os campos que são obrigatórios no model ***
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()
    # comentarios = ComentarioSerializer(many=True, read_only=True)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'descricao_completa', 'descricao_completa2', 'aprovado', 'foto', 'atracoes', 'avaliacoes', 'comentarios', 'endereco', 'doc_identificacao'
        )
        # *** Corresponde ao read_only=True, quando não são campos extras
        read_only_fields = ('comentarios',)

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objects.create(**endereco)

        avaliacoes = validated_data['avaliacoes']
        del validated_data['avaliacoes']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doc1 = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        ponto.avaliacoes.set(avaliacoes)

        ponto.endereco = end
        ponto.doc_identificacao = doc1

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s ' % (obj.nome, obj.descricao)

