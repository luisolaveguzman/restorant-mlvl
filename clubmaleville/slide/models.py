from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo', null=True, blank=True)
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='slides')
    url = models.URLField(verbose_name='Enlace', null=True, blank=True)

    class Meta:
        verbose_name='slide'
        verbose_name_plural='slides'
        ordering = ['-id']

    def __str__(self):
        return self.title