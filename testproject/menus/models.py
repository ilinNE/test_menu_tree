from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    slug = models.SlugField(verbose_name="Слаг")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    url = models.CharField(max_length=256, verbose_name="Адрес")
    parent = models.ForeignKey(
        "MenuItem",
        blank=True,
        null=True,
        related_name="children",
        verbose_name="Родительский элемент",
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(
        "Menu",
        blank=True,
        null=True,
        related_name="elements",
        verbose_name="Menu",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.name
