from siteblocks.models import Menu
from django import template

register = template.Library()


def get_active_menu(url, site_menu):
    for i, menu_item in enumerate(site_menu):
        setattr(site_menu[i], 'is_active', False)
        if url.find(menu_item.url) == 0:
            site_menu[i].is_active = True
    return site_menu


@register.inclusion_tag("siteblocks/menu.html")
def menu(url):
    menu = Menu.objects.filter(visible=True)
    menu = get_active_menu(url, menu)
    return {'menu': menu}
