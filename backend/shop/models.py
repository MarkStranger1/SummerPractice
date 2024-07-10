"""
Содержит модели для следующих объектов:

- Город;
- Улица;
- Магазин.
"""

from django.conf import settings
from django.db import models


class Abstract(models.Model):
    """Абстрактная модель для моделей City и Street."""
    name = models.CharField(
        verbose_name="Название",
        max_length=settings.LIMIT_CHAR_200,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class City(Abstract):
    """Модель для объекта Город."""

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        default_related_name = "Cities"


class Street(Abstract):
    """Модель для объекта Улица."""

    city = models.ForeignKey(
        City,
        verbose_name="Город",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        default_related_name = "Streets"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "city"],
                name="unique_street_city",
            )
        ]


class Shop(Abstract):
    """Модель для объекта Магазин."""

    street = models.ForeignKey(
        Street,
        verbose_name="Улица",
        on_delete=models.CASCADE,
    )
    house = models.PositiveSmallIntegerField(
        verbose_name="Номер дома",
    )
    open_time = models.TimeField(
        verbose_name="Время открытия",
    )
    close_time = models.TimeField(
        verbose_name="Время закрытия",
    )

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        default_related_name = "Shops"
