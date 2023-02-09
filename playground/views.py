from django.shortcuts import render
from django.db.models import Value, F, Func,ExpressionWrapper,DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer
# Create your views here.


def say_hello(request):
    discounted_price = ExpressionWrapper(F('unit_price')*0.8, output_field=DecimalField())
    result = Product.objects.annotate(
        discounted_price=discounted_price)  # search "django database functions" for more

    return render(request, 'hello.html', {'name': 'amir', 'result': result})
