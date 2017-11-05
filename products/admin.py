from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 0


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0


class ProductToCategoryInline(admin.TabularInline):
    model = ProductToCategory
    extra = 0


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug', 'is_active', 'created', 'changed')  # Sane defaults.

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "full_name", "slug", "vendor_code", 'category', "price", "is_active", "changed")
    list_display_links = ('name', "full_name", 'slug',)
    list_filter = []
    list_editable = ('category', 'is_active',)
    search_fields = ('name', 'price', 'vendor_code',)

    prepopulated_fields = {'slug': ('name',)}
    list_select_related = True
    # list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline, ProductToCategoryInline, ProductReviewInline, ProductColorInline, ProductAttributeInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductReview._meta.fields]

    class Meta:
        model = ProductReview


admin.site.register(ProductReview, ProductReviewAdmin)
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
