from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    queryset = TaggedItem.objects.values('objects')
    return render(request, 'hello.html', {'name': 'amir', 'tags': queryset})
