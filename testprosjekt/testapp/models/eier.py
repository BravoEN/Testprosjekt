from django.db import models

class Eier(models.Model):
    fornavn = models.CharField(max_length=40)
    etternavn = models.CharField(max_length=40)
    adresse = models.CharField(max_length=100)
    tlf_landskode = models.IntegerField(max_length=5)

    def __str__(self):
        return self.fornavn