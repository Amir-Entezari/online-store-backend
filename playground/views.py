from django.shortcuts import render
from django.db import connection
from store.models import Product


def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')
    # OR
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM store_product')
    return render(request, 'hello.html', {'name': 'amir'})
