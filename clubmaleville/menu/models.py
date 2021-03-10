from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    condition = models.BooleanField(verbose_name='Activo', null=True, blank=True)


    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering = ['id']

    def __str__(self):
            return self.name

class Carta(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    image = models.ImageField(verbose_name='Imagen', upload_to='Carta', null=True, blank=True)
    category =models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)

    class Meta:
        verbose_name='plato'
        verbose_name_plural='platos'
        ordering = ['id']

    def __str__(self):
            return f"{self.name}"
