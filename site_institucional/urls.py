from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from administracao.views import ContatoViewSet
from administracao.views import ColaboradorViewSet
from administracao.views import ConfiguracaoGeralViewSet
from administracao.views import ServicoViewSet
from administracao.views import ServicoPortfolioViewSet
from administracao.views import index

router = routers.DefaultRouter()
router.register(r'configuracoes_gerais', ConfiguracaoGeralViewSet)
router.register(r'contatos', ContatoViewSet)
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'servicos_portfolio', ServicoPortfolioViewSet)

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
