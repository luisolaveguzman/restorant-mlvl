from django.db import models

# Create your models here.
class MenuDiario(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    price = models.IntegerField(verbose_name='Precio')

    class Meta:
        verbose_name='fondo'
        verbose_name_plural='fondos'
        ordering = ['id']

    def __str__(self):
            return f"{self.name}"

class Entrada(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    condition = models.BooleanField(verbose_name='Activo')

    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
        ordering = ['id']

    def __str__(self):
            return f"{self.name}"

class Acompanamiento(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    condition = models.BooleanField(verbose_name='Activo')

    class Meta:
        verbose_name='acompañamiento'
        verbose_name_plural='acompañamientos'
        ordering = ['id']

    def __str__(self):
            return f"{self.name}"

class Especialidades(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    price = models.IntegerField(verbose_name='Precio', null=True, blank=True)
    condition = models.BooleanField(verbose_name='Activo')

    class Meta:
        verbose_name='especial'
        verbose_name_plural='especialidades'
        ordering = ['id']

    def __str__(self):
            return f"{self.name}"