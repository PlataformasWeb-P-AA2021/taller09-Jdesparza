from django.db import models

# Create your models here.
class Parroquia(models.Model):
    class Meta:
        ordering = ["tipo"]
        verbose_name_plural = "Las Parroquias"

    opciones_tipo_parroquia = (
        ('1', 'urbana'),
        ('2', 'rural'),
        )

    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_parroquia) 


    def __str__(self):
        return "%s - tipo: %s" % (
                self.nombre,
                self.tipo)


class Barrio(models.Model):
    class Meta:
        verbose_name_plural = "Los Barrios"

    opciones_numero_parques = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        )

    nombre = models.CharField(max_length=50)
    numero_viviendas = models.IntegerField()
    numero_parques = models.CharField(max_length=30, \
            choices=opciones_numero_parques) 
    numero_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, related_name='losbarrios', 
            on_delete=models.CASCADE)


    def __str__(self):
        return "%s - %d - %s - %d - Parroquia(%s)" % (
                self.nombre,
                self.numero_viviendas,
                self.numero_parques,
                self.numero_edificios,
                self.parroquia.nombre
                )