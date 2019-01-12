from django.contrib import admin
from .models import Product, Order
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.html import format_html


# Register your models here.

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductAdmin(AdminImageMixin, ImportExportModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="auto" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    list_display = [
        'image_tag',
        'id',
        'name',
        'type',
        'brand',
        'sub_brand',
        'price',
        'description',
        'in_stock',
    ]
    list_filter = [
        'price',
        'brand',
        'sub_brand',
        'type',
    ]
    list_editable = [
        'in_stock',
        'sub_brand',
    ]

    search_fields = [
          'id',
          'name',
          'type',
          'brand',
          'sub_brand'
    ]

    list_per_page = 20


    resource_class = ProductResource


admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):

    def name(self,obj):
        return obj.first_name + ' ' + obj.last_name
    list_display = [
        'date',
        'name',
        'email',
        'collection_date',
        'paid'
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email'
    ]

    list_editable = [
        'paid'
    ]
    list_filter = [
        'paid'
    ]

admin.site.register(Order, OrderAdmin)

admin.site.site_header = 'Backpacks TT Admin'
admin.site.site_title = 'Backpacks TT'
admin.site.index_title = 'Backpacks TT'

