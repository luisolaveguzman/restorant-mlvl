from django.db import models

class Contact(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=255, null=True, blank=True)
    mail = models.EmailField(verbose_name='Correo', max_length=255)
    content = models.TextField(verbose_name='Mensaje', null=True, blank=True)

    class Meta:
        verbose_name='Contacto'
        verbose_name_plural='Contactos'
        ordering = ['-id']

    def __str__(self):
        return self.name