from django import template

from menus.models import MenuItem
from menus.templatetags.utils import build_menu_tree

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu):
    queryset = (
        MenuItem.objects.select_related("parent")
        .values("id", "url", "name", "parent_id")
        .filter(menu__slug=menu)
        .order_by("-parent__id")
    )
    url = context.request.path
    items = build_menu_tree(queryset, url)
    return {"items": items, "url": url}


@register.inclusion_tag("item.html")
def draw_item(item, url):
    return {"item": item, "url": url}
