# Generated by Django 3.1.7 on 2021-03-08 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MenuDiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menudiario.title', verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
                'ordering': ['id'],
            },
        ),
    ]