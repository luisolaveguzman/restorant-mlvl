# Generated by Django 3.1.7 on 2021-03-08 02:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Subtitulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='slides', verbose_name='Imagen')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
            ],
            options={
                'verbose_name': 'slide',
                'verbose_name_plural': 'slides',
                'ordering': ['-id'],
            },
        ),
    ]