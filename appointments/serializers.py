from rest_framework import serializers
from appointments.models import Appointment
from datetime import datetime
from professionals.models import Professionals


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'date', 'professional')
        
    def validate_date(self, value):
        if value < datetime.now():
            raise serializers.ValidationError('A data da consulta deve ser no futuro')
        return value
    
    def validate_professional(self, value):
        if not Professionals.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError('Profissional não encontrado.')
        return value