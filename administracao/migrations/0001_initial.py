# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.FileField(upload_to='')),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracaoGeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('sobre_nos', models.TextField(blank=True, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('telefone', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('mensagem', models.TextField()),
                ('visualizado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='')),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]