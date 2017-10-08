from django.contrib import admin

from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'visible',)
    list_display_links = ('title', 'slug',)
    list_editable = ('visible', 'order', )
    search_fields = ('title', 'slug', 'content',)

    prepopulated_fields = {'slug': ('title',)}
    list_select_related = True


admin.site.register(Page, PageAdmin)
