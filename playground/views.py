from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    Collection.objects.update(title='Games')  # This method is recommonded
    # OR
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    return render(request, 'hello.html', {'name': 'amir'})
