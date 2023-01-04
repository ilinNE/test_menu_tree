from django.contrib import admin

from menus.models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = (MenuItemInline,)


admin.site.register(Menu, MenuAdmin)
