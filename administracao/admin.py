from django.contrib import admin
from administracao.models import Colaborador
from administracao.models import ConfiguracaoGeral
from administracao.models import Contato
from administracao.models import Servico
from administracao.models import ServicoPortfolio

@admin.register(ConfiguracaoGeral)
class ConfiguracaoGeralAdmin(admin.ModelAdmin):
    pass
    # list_display = ('nome', 'telefone', 'endereco',)

admin.site.register(Contato)
admin.site.register(Colaborador)
admin.site.register(Servico)
admin.site.register(ServicoPortfolio)
