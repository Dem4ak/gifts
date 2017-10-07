from siteblocks.models import Menu
from django.contrib import admin


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'visible',)
    list_display_links = ('title',)
    list_editable = ('order', 'visible',)
    list_filter = ('visible',)


admin.site.register(Menu, MenuAdmin)
