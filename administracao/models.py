from django.db import models


class ConfiguracaoGeral(models.Model):
    
	titulo = models.CharField(max_length=40)
	sobre_nos = models.TextField(null=True, blank=True)
	endereco = models.TextField(null=True, blank=True)
	telefone = models.CharField(max_length=20)
	ativo = models.BooleanField(default=False)
	area_de_colaboradores = models.BooleanField(default=False)
	area_de_servicos = models.BooleanField(default=False)
	area_de_contatos = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.ativo:
			self.__class__.objects.all().update(ativo=False)
		super(ConfiguracaoGeral, self).save(*args, **kwargs)
	

class Servico(models.Model):
    
	foto = models.FileField()
	descricao = models.TextField(null=True, blank=True)

    
class Colaborador(models.Model):
	
	nome = models.CharField(max_length=40)
	descricao = models.TextField(null=True, blank=True)
	foto = models.FileField()
	ativo = models.BooleanField(default=False)


class Contato(models.Model):
	
	nome = models.CharField(max_length=40)
	telefone = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	mensagem = models.TextField()
	visualizado = models.BooleanField(default=False)