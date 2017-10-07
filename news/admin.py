from django.contrib import admin

from news.models import NewsCategory, News


# class NewsCategoryInline(admin.TabularInline):
#     model = News
#     extra = 0


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewsCategory._meta.fields]
    list_display_links = ('name',)
    list_editable = ('is_active',)
    search_fields = ('name',)

    list_select_related = True

    class Meta:
        model = NewsCategory


admin.site.register(NewsCategory, NewsCategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug", "category", "visible", ]
    list_display_links = ('title', 'slug',)
    list_editable = ('visible',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('title',)}
    list_select_related = True

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
