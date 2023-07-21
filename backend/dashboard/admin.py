from django.contrib import admin
from dashboard.models import Order, Product, Deliveryman


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Deliveryman)
class DeliverymanAdmin(admin.ModelAdmin):
    ...
