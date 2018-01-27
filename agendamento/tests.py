# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Agendamento, Paciente, Procedimento

class TesteAgendamento(TestCase):
    def setUp(self):
        procedimento, novo = Procedimento.objects.get_or_create(nome="Procedimento A")
        paciente, novo = Paciente.objects.get_or_create(nome="João Zalé")

        self.agendamento = Agendamento.objects.create(
            data="2022-10-12",
            horario_inicio="16:00:22",
            horario_fim="16:30:22",
            paciente=paciente,
            procedimento=procedimento
            )

    def tearDown(self):
        pass

    def testObjetosCriados(self):
        self.assertEquals(Procedimento.objects.count(), 1)
        self.assertEquals(Paciente.objects.count(), 1)
        self.assertEquals(Agendamento.objects.count(), 1)
