# Generated by Django 5.0.6 on 2024-05-31 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_remove_factura_cliente_alter_factura_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Moneda',
            field=models.CharField(blank=True, default='USD', max_length=10, null=True),
        ),
    ]
