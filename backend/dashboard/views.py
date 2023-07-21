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


def search(request):
    order_id = request.GET.get('orderid', '0')
    deliveryman = request.GET.get('deliveryman', '')
    order = Order.objects.filter(id=order_id).first() or Order.objects.filter(deliveryman=deliveryman).first()
    return render(request, 'dashboard/pages/search.html',
                  {
                      'order': order
                  })
