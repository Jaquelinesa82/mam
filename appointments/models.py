from django.db import models
from professionals.models import Professionals


class Appointment(models.Model):
    date = models.DateTimeField()
    professional = models.ForeignKey(Professionals, on_delete=models.CASCADE, related_name='appointtments')
    
    def __str__(self):
        return f'Consulta com {self.professional.name} em {self.date}'
