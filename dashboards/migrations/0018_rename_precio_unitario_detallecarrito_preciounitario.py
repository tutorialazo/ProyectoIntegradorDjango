# Generated by Django 5.0.6 on 2024-06-11 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0017_remove_carrito_orden_asociada_carrito_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecarrito',
            old_name='precio_unitario',
            new_name='precioUnitario',
        ),
    ]
