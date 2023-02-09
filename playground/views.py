from django.shortcuts import render
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer
# Create your views here.


def say_hello(request):
    result = Customer.objects.annotate(
        orders_count=Count('order'))  # search "django database functions" for more

    return render(request, 'hello.html', {'name': 'amir', 'result': result})
