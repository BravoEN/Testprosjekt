from django.db import models
from . import Eier

class Hund(models.Model):
    navn = models.CharField(max_length=40)
    rase = models.CharField(max_length=40)
    eier = models.ForeignKey(Eier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.navn