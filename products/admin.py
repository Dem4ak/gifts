from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0


class ProductCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug', 'is_active', 'created', 'changed')  # Sane defaults.

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "full_name", "slug", "vendor_code", 'categories', "price", "is_active", "changed")
    list_display_links = ('name', "full_name", 'slug',)
    list_filter = []
    list_editable = ('categories', 'is_active',)
    search_fields = ('name', 'price', 'vendor_code',)

    prepopulated_fields = {'slug': ('name',)}
    list_select_related = True
    # list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline, ProductColorInline, ProductAttributeInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductImage._meta.fields]
#
#     class Meta:
#         model = ProductImage
#
#
# admin.site.register(ProductImage, ProductImageAdmin)
#
#
# class ProductColorAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductColor._meta.fields]
#
#     class Meta:
#         model = ProductColor
#
#
# admin.site.register(ProductColor, ProductColorAdmin)
#
#
# class ProductAttributeAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductAttribute._meta.fields]
#
#     class Meta:
#         model = ProductAttribute
#
#
# admin.site.register(ProductAttribute, ProductAttributeAdmin)
