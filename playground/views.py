from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem
# Create your views here.


def say_hello(request):
    queryset = Product.objects.prefetch_related('promotion').select_related('collection').all()  # search for more: queryset api

    return render(request, 'hello.html', {'name': 'amir', 'products': list(queryset)})
