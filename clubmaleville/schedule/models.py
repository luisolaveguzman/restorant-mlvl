from django.db import models

# Create your models here.
class Schedule(models.Model):
    days = models.CharField(max_length=255, verbose_name='dias')
    schedule = models.CharField(max_length=255, verbose_name='Horario')

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'
        ordering=['id']

    def __str__(self):
        return self.days

