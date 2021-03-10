# Generated by Django 3.1.7 on 2021-03-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menudiario', '0004_delete_acompanamiento'),
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
    ]
