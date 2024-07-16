from django.db import models

# Creclass Curso(models.Model):
class Usuario(models.Model):
    telefono = models.CharField(primary_key=True, max_length=15)
    nombreC = models.CharField(max_length=100)
    nombreR = models.CharField(max_length=100)
    tiempoH = models.PositiveSmallIntegerField()
    mensaje = models.CharField(max_length=500)
    campo11 = models.DateTimeField()
    campo12 = models.DurationField()
    campo13 = models.IntegerField()
    campo1 = models.IntegerField()
    campo3 = models.CharField(max_length=100)
    campo4 = models.CharField(max_length=100)
    campo5 = models.CharField(max_length=100)
    campo6 = models.CharField(max_length=100)
   

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreC, self.tiempoH)
