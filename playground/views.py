from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'name': 'amir'})
