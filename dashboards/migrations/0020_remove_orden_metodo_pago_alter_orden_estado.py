# Generated by Django 5.0.6 on 2024-06-11 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0019_rename_fecha_creacion_carrito_creado_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='metodo_pago',
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(default='Completado', max_length=100),
        ),
    ]
