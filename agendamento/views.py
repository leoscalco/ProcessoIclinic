# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from agendamento.serializers import *
from agendamento.models import Agendamento

class AgendamentoList(APIView):

    def get(self, request, format=None):
        """
        List all agendamentos in database.
        """
        agendamento = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamento, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new Agendamento instance.
        """

        serializer = AgendamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgendamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Agendamento.objects.get(pk=pk)
        except Agendamento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Detail an Agendamento instance.
        """
        agendamento = self.get_object(pk)
        serializer = AgendamentoSerializer(agendamento)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update an Agendamento instance.
        """
        agendamento = self.get_object(pk)

        serializer = AgendamentoSerializer(agendamento, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete an Agendamento instance.
        """
        agendamento = self.get_object(pk)
        Agendamento.delete(agendamento)
        return Response(status=status.HTTP_204_NO_CONTENT)