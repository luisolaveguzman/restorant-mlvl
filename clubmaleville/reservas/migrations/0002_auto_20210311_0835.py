# Generated by Django 3.1.7 on 2021-03-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]
