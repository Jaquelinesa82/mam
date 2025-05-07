from rest_framework import serializers
from .models import Professionals


class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionals
        fields = (
            'id', 'name', 'profession', 'address', 'contact'
        )