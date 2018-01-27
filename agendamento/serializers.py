from rest_framework import serializers

from .models import Agendamento, Paciente, Procedimento
from django.db import IntegrityError, transaction


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
            'id','nome'
            )

class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = (
            'id', 'nome'
            )

class AgendamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    procedimento = ProcedimentoSerializer()
    class Meta:
        model = Agendamento
        fields = (
            'id', 'data', 'horario_inicio', 'horario_fim',
            'paciente', 'procedimento'
            )

    def create(self, validated_data):
        try:
            with transaction.atomic():
                paciente = Paciente.objects.create(nome=validated_data['paciente']['nome'])
                procedimento = Procedimento.objects.create(nome=validated_data['procedimento']['nome'])

                instance = Agendamento.objects.create(
                    data=validated_data['data'],
                    horario_inicio=validated_data['horario_inicio'],
                    horario_fim=validated_data['horario_fim'],
                    paciente=paciente,
                    procedimento=procedimento
                    )
                return instance

        except IntegrityError:
            return "IntegrityError at AgendamentoSerializer"

    def update(self, instance, validated_data):
        try:
            with transaction.atomic():
                instance.paciente.nome = validated_data['paciente']['nome']
                instance.paciente.save()

                instance.procedimento.nome = validated_data['procedimento']['nome']
                instance.procedimento.save()

                instance.data = validated_data['data']
                instance.horario_inicio = validated_data['horario_inicio']
                instance.horario_fim = validated_data['horario_fim']
                instance.save()
                return instance

        except IntegrityError:
            return "IntegrityError at AgendamentoSerializer"