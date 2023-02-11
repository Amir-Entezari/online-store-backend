from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models
# Register your models here.


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 20

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        else:
            return "OK"


admin.site.register(models.Promotion)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 20


admin.site.register(models.Address)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at',
                    'payment_status', 'customer']
    list_select_related = ['customer']
    ordering = ['-placed_at']
    list_per_page = 20


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'quantity', 'unit_price']
    ordering = ['order__placed_at']


admin.site.register(models.Cart)
admin.site.register(models.CartItem)
