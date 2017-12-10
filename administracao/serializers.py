from rest_framework import serializers
from administracao.models import ConfiguracaoGeral
from administracao.models import Contato
from administracao.models import Colaborador
from administracao.models import Servico


class ContatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'


class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'
        

class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class ConfiguracaoGeralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfiguracaoGeral
        fields = '__all__'