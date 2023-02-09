from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    queryset = Product.objects.values('id','title','unit_price','collection__title') # search for more: queryset api

    return render(request, 'hello.html', {'name': 'amir', 'products': list(queryset)})
