from django.shortcuts import render
from django.db.models import Value,F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product,Customer
# Create your views here.


def say_hello(request):
    result = Customer.objects.annotate(is_new=Value(True),new_id=F('id')+1)

    return render(request, 'hello.html', {'name': 'amir', 'result': result})
