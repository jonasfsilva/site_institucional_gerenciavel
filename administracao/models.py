from django.db import models


class ConfiguracaoGeral(models.Model):
    
	titulo = models.CharField(max_length=40)
	endereco = models.TextField(null=True, blank=True)
	telefone = models.CharField(max_length=20)
	ativo = models.BooleanField(default=False)
	
	area_de_servicos = models.BooleanField(default=False)
	area_de_sobrenos = models.BooleanField(default=False)
	area_de_apresentacao = models.BooleanField(default=False)
	area_de_colaboradores = models.BooleanField(default=False)
	area_de_contatos = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.ativo:
			self.__class__.objects.all().update(ativo=False)
		super(ConfiguracaoGeral, self).save(*args, **kwargs)
	

class Servico(models.Model):
	foto = models.FileField()
	descricao = models.TextField(null=True, blank=True)


class ConfiguracaoServico(models.Model):
	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	servicos = models.ManyToManyField(Servico)

    
class Colaborador(models.Model):
	nome = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	foto = models.FileField()
	ativo = models.BooleanField(default=False)


class ConfiguracaoColaborador(models.Model):
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
	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)


class Acontecimento(models.Model):
	titulo = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	foto = models.FileField()
	ativo = models.BooleanField(default=False)


class ConfiguracaoSobreNos(models.Model):
	titulo = models.CharField(max_length=40)
	acontecimentos = models.ManyToManyField(Acontecimento)