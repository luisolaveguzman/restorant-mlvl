# Generated by Django 3.1.7 on 2021-03-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menudiario', '0002_auto_20210308_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('condition', models.BooleanField(verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'acompañamiento',
                'verbose_name_plural': 'acompañamientos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('condition', models.BooleanField(verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'entrada',
                'verbose_name_plural': 'entradas',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='menudiario',
            name='content',
        ),
    ]