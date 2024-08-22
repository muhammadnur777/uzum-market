from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import Category, Product, ProductImage, Color

class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = ('image', 'product')


class ColorStackedInline(StackedInline):
    model = Color
    fields = ('name', 'product')


@register(Product)
class ProductModelsAdmin(ModelAdmin):
    inlines = ProductImageStackedInline, ColorStackedInline 
    list_display = 'name', 'category', 'narxi', 'quantity'

@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass



