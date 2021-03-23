# Generated by Django 3.1.7 on 2021-03-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('mail', models.EmailField(max_length=255, verbose_name='Correo')),
                ('phone', models.IntegerField(max_length=255, verbose_name='Telefono')),
                ('date', models.DateField(verbose_name='Fecha reserva')),
                ('hour', models.TimeField(verbose_name='Hora')),
                ('cant', models.SmallIntegerField(verbose_name='Cantidad de personas')),
                ('detail', models.TextField(verbose_name='Detalle')),
            ],
            options={
                'verbose_name': 'reserva',
                'verbose_name_plural': 'reservas',
                'ordering': ['-id'],
            },
        ),
    ]
