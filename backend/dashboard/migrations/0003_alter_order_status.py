# Generated by Django 4.2 on 2023-07-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_deliveryman_order_order_deliveryman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Atrasado', 'ATRASADO'), ('A caminho', 'A_CAMINHO'), ('entregue', 'ENTREGUE'), ('Preparando pedido', 'PREPARANDO_PEDIDO')], default='PREPARANDO_PEDIDO', max_length=20),
        ),
    ]
