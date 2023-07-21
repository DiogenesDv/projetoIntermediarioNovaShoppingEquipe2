from django.db import models


STATUS_CHOICES = (
    ('ATRASADO', 'Atrasado'),
    ('A_CAMINHO', 'A caminho'),
    ('ENTREGUE', 'Entregue'),
    ('PREPARANDO_PEDIDO', 'Preparando pedido')
)


class Deliveryman(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PREPARANDO_PEDIDO'
    )
    deliveryman = models.ForeignKey(Deliveryman, on_delete=models.SET_NULL, null=True)  # noqa
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.product.title
