from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug', 'is_active', 'created', 'changed')  # Sane defaults.

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "vendor_code", "price", "is_active", "changed")
    list_display_links = ('name', 'slug',)
    list_filter = []
    list_editable = ('is_active',)
    search_fields = ('name', 'price', 'category', 'vendor_code',)

    prepopulated_fields = {'slug': ('name',)}
    list_select_related = True
    # list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
