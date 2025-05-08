from rest_framework import serializers
from .models import Professionals


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionals
        fields = (
            'id', 'name', 'profession', 'address', 'contact'
        )
        
    def validate_name(self, value):
        return value.strip().title()
    
    def validate_profession(self, value):
        return value.strip().title()
    
    def validate_address(self, value):
        return value.strip()
    
    def validate_contact(self, value):
        cleaned = value.strip().replace(" ", "").replace("-", "")
        if not cleaned.isdigit():
            raise serializers.ValidationError('O contato deve conter apenas números')
        if len(cleaned) < 10:
            raise serializers.ValidationError('O contato deve ter pelo menos 10 dígitos.')
        return cleaned