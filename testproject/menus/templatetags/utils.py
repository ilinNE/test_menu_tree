from django.urls import reverse, exceptions
from django.db.models import QuerySet


def find_children(item_dict: dict, children: dict) -> None:
    try:
        item_dict["children"] = children[item_dict["id"]]
        for child in item_dict["children"]:
            find_children(child, children)
    except KeyError:
        pass


def find_opened_items(items: list, url: str):
    for item in items:
        item['is_opened'] = True
        if item['url'] == url:
            return False
        if not find_opened_items(item.get('children', []), url):
            return False
    return True


def build_menu_tree(queryset: QuerySet, url) -> list:
    result = []
    children = {}
    for item in queryset:
        item_dict = {"id": item["id"], "name": item["name"], "is_opened": False}
        try:
            url = reverse(item["url"])
        except exceptions.NoReverseMatch:
            url = item["url"]
        item_dict["url"] = url
        if item["parent_id"] is None:
            find_children(item_dict, children)
            result.append(item_dict)
            continue
        if children.get(item["parent_id"]):
            children[item["parent_id"]].append(item_dict)
        else:
            children[item["parent_id"]] = [
                item_dict,
            ]
    find_opened_items(result, url)
    return result
