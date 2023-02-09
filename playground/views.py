from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.


def say_hello(request):
    query_set = Product.objects.all()

    return render(request, 'hello.html', {'name': 'amir'})
