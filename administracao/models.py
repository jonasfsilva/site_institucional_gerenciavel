from django.db import models


class ConfiguracaoGeral(models.Model):
    	
	class Meta:
		verbose_name_plural = 'Configurações Gerais'
    
	titulo = models.CharField(max_length=40, verbose_name='Titulo do Site')
	endereco = models.TextField(null=True, blank=True, verbose_name='Endereço da Empresa')
	telefone = models.CharField(max_length=20)
	ativo = models.BooleanField(default=False, verbose_name='Esta configuração esta ativa?')
	
	area_de_servicos = models.BooleanField(default=False, verbose_name='Exibir area de servicos?')
	area_de_sobrenos = models.BooleanField(default=False, verbose_name='Exibir area sobre nós?')
	area_de_apresentacao = models.BooleanField(default=False, verbose_name='Exibir area de apresentacao?')
	area_de_colaboradores = models.BooleanField(default=False, verbose_name='Exibir area com equipe?')
	area_de_contatos = models.BooleanField(default=False, verbose_name='Exibir area para contatos?')

	def save(self, *args, **kwargs):
		if self.ativo:
			self.__class__.objects.all().update(ativo=False)
		super(ConfiguracaoGeral, self).save(*args, **kwargs)
	

class Servico(models.Model):
	foto = models.FileField()
	descricao = models.TextField(null=True, blank=True)


class ConfiguracaoServico(models.Model):
    
	class Meta:
		verbose_name_plural = 'Configurações Serviços'

	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	servicos = models.ManyToManyField(Servico)

    
class Colaborador(models.Model):
    
	class Meta:
		verbose_name_plural = 'Colaboradores'

	nome = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	foto = models.FileField()
	ativo = models.BooleanField(default=False, verbose_name='Exibir este colaborador?')


class ConfiguracaoColaborador(models.Model):
	
	class Meta:
		verbose_name_plural = 'Configurações Colaboradores'

	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	colaboradores = models.ManyToManyField(Colaborador)


class Contato(models.Model):
	nome = models.CharField(max_length=40)
	telefone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	mensagem = models.TextField()
	visualizado = models.BooleanField(default=False)


class ConfiguracaoContato(models.Model):
    
	class Meta:
		verbose_name_plural = 'Configurações Textos em Contatos'

	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)


class Acontecimento(models.Model):
	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	foto = models.FileField()
	ativo = models.BooleanField(default=False)


class ConfiguracaoSobreNos(models.Model):
	
	class Meta:
		verbose_name_plural = 'Configurações da area sobre nós'

	titulo = models.CharField(max_length=40)
	acontecimentos = models.ManyToManyField(Acontecimento)