from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem,Order
# Create your views here.


def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[:5]  # search for more: queryset api

    return render(request, 'hello.html', {'name': 'amir', 'orders': list(queryset)})
