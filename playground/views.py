from django.shortcuts import render
from django.db.models import Value, F, Func
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer
# Create your views here.


def say_hello(request):
    result = Customer.objects.annotate(full_name=Func(
        F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    return render(request, 'hello.html', {'name': 'amir', 'result': result})
