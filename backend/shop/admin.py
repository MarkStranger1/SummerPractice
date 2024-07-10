"""
Содержит настройку Admin-панели для моделей:

- City;
- Street;
- Shop.
"""

from django.contrib import admin
from shop.models import City, Shop, Street


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Admin-панель для модели Сity."""
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    """Admin-панель для модели Street."""
    list_display = ('id', 'name', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    """Admin-панель для модели Shop."""
    list_display = ('id', 'name', 'street', 'house', 'open_time', 'close_time')
    search_fields = ('name', 'street__name', 'street__city__name', 'house')
    list_filter = ('street__city', 'street')
