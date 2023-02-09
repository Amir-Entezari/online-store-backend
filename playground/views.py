from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    queryset = Product.objects.filter(collection__id__range=(3,6)) #search for more: queryset api
    print(queryset[0])

    return render(request, 'hello.html', {'name': 'amir','products':list(queryset)})
