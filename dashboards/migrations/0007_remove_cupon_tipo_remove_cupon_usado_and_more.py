# Generated by Django 5.0.6 on 2024-05-27 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0006_alter_cliente_imagen_alter_producto_imagen_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cupon',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='cupon',
            name='usado',
        ),
        migrations.AlterField(
            model_name='cupon',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cupones_utilizados', to=settings.AUTH_USER_MODEL),
        ),
    ]
