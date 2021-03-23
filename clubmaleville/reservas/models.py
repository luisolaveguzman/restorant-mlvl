from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    mail = models.EmailField(max_length=255, verbose_name='Correo')
    phone = models.IntegerField(verbose_name='Telefono')
    date = models.DateField(verbose_name='Fecha reserva')
    hour = models.TimeField(verbose_name='Hora')
    cant = models.SmallIntegerField(verbose_name='Cantidad de personas')
    detail = models.TextField(verbose_name='Detalle', null=True, blank=True)
    state = models.BooleanField(verbose_name='Estado', default=True)

    class Meta:
        verbose_name='reserva'
        verbose_name_plural='reservas'
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'