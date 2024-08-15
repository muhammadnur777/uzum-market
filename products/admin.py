from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import Category, Product, ProductImage

class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = ('image', 'product')


@register(Product)
class ProductModelsAdmin(ModelAdmin):
    inlines = ProductImageStackedInline, 


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass

