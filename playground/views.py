from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product
# Create your views here.


def say_hello(request):
    result = Product.objects.aggregate(Count('id'),min_price=Min('unit_price'))  # search for more: queryset api

    return render(request, 'hello.html', {'name': 'amir', 'result': result})
