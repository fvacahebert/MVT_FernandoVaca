from django.db import models

# Create your models here.

class Familia(models.Model):
    DNI=models.IntegerField()
    nombre=models.CharField(max_length=50)
    parentezco=models.CharField(max_length=50)
    fecha_de_cumpleaños=models.CharField(max_length=50)

    def __str__(self):
        return str(self.DNI)+" "+self.nombre+" "+self.parentezco+" "+self.fecha_de_cumpleaños
    

