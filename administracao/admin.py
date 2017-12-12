from django.contrib import admin
from administracao.models import Colaborador
from administracao.models import ConfiguracaoColaborador
from administracao.models import ConfiguracaoGeral
from administracao.models import Contato
from administracao.models import ConfiguracaoContato
from administracao.models import Servico
from administracao.models import ConfiguracaoServico
from administracao.models import Acontecimento
from administracao.models import ConfiguracaoSobreNos

@admin.register(ConfiguracaoGeral)
class ConfiguracaoGeralAdmin(admin.ModelAdmin):
    pass
    # list_display = ('nome', 'telefone', 'endereco',)

admin.site.register(Contato)
admin.site.register(ConfiguracaoContato)
admin.site.register(Colaborador)
admin.site.register(ConfiguracaoColaborador)
admin.site.register(Servico)
admin.site.register(ConfiguracaoServico)
admin.site.register(Acontecimento)
admin.site.register(ConfiguracaoSobreNos)
