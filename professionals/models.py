from django.db import models


class Professionals(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name