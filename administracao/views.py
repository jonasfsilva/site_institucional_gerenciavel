from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from administracao.models import ConfiguracaoGeral
from administracao.models import Contato
from administracao.models import Colaborador
from administracao.models import Servico
from administracao.models import ServicoPortfolio
from administracao.serializers import ContatoSerializer
from administracao.serializers import ServicoSerializer
from administracao.serializers import ColaboradorSerializer
from administracao.serializers import ConfiguracaoGeralSerializer
from administracao.serializers import ServicoPortfolioSerializer

def index(request):
    return render(request, 'index.html', {})


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ConfiguracaoGeralViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracaoGeral.objects.all()
    serializer_class = ConfiguracaoGeralSerializer


class ServicoPortfolioViewSet(viewsets.ModelViewSet):
    queryset = ServicoPortfolio.objects.all()
    serializer_class = ServicoPortfolioSerializer