"""
Содержит фильтры для моделей:

- Shop;
- ...
"""

from datetime import datetime

from django_filters.rest_framework import FilterSet, filters
from shop.models import Shop

"""
Определяем класс ShopFilter, который используется для фильтрации 
объектов модели Shop с помощью библиотеки django-filter
"""


class ShopFilter(FilterSet):
    """
    Фильтрация для модели Shop по городу,
    улице и статусу (открыт/закрыт).
    """

    street = filters.CharFilter(field_name='street__name',
                                lookup_expr='icontains')
    city = filters.CharFilter(field_name='street__city__name',
                              lookup_expr='icontains')
    open = filters.NumberFilter(method='filter_open')

    """
    Определяем модель, к которой применяется фильтр
    """
    class Meta:
        model = Shop
        fields = ['street', 'city', 'open']

    """
    Используем filter_open для фильтрации по статусу "открыт/закрыт"
    """
    def filter_open(self, queryset, name, value):
        """Фильтрация по статусу (открыт/закрыт)."""
        current_time = datetime.now().time()

        if value == 1:
            return queryset.filter(open_time__lte=current_time,
                                   close_time__gte=current_time)
        elif value == 0:
            closed_morning = queryset.filter(open_time__gte=current_time)
            closed_evening = queryset.filter(close_time__lte=current_time)
            return closed_morning | closed_evening
        return queryset
