# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    # aqui poderiam vir outros campos para paciente.

class Procedimento(models.Model):
    nome = models.CharField(max_length=200)
    # aqui poderiam vir outros campos para procedimento.

class Agendamento(models.Model):
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    paciente = models.ForeignKey(Paciente)
    procedimento = models.ForeignKey(Procedimento)

