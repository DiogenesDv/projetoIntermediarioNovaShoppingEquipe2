from django.shortcuts import render
from dashboard.models import Order


def index(request):
    orders = Order.objects.all()
    orders_atrasados = Order.objects.filter(status='ATRASADO')
    return render(request, 'dashboard/pages/index.html',
                  {
                      'orders': orders,
                      'orders_atrasados': orders_atrasados
                  })
