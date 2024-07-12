"""
Содержит преобразователи данных(сериализаторы) для моделей:

- City;
- Street;
- Shop.
"""

from rest_framework import serializers
from shop.models import City, Shop, Street

"""
Сериализатор, который преобразует данные модели City в формат JSON. 
Он использует ModelSerializer для автоматического определения полей и настроек сериализации.
"""


class CitySerializer(serializers.ModelSerializer):
    """Преобразование данных модели City."""

    class Meta:
        model = City
        fields = (
            "id",
            "name",
        )


"""
Сериализатор, который преобразует данные модели Street в JSON-формат, содержащий только поля id и name
"""


class ShortStreetSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Short."""

    class Meta:
        model = Street
        fields = (
            "id",
            "name",
        )


"""
Сериализатор используется для записи данных в модель Shop, где значения поля city получаются из связанных моделей,
а поле street представляет собой идентификатор объекта Street
"""


class ShopWriteSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Shop на запись."""

    city = serializers.CharField(
        source='street.city.name', read_only=True
    )
    street = serializers.PrimaryKeyRelatedField(queryset=Street.objects.all())

    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "city",
            "street",
            "house",
            "open_time",
            "close_time",
        )


"""
Сериализатор ShopReadSerializer, который используется для вывода данных модели Shop
Автоматически создает поля сериализатора на основе модели Shop
"""


class ShopReadSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Shop на чтение."""

    city = serializers.CharField(
        source='street.city.name', read_only=True
    )
    street = serializers.CharField(
        source='street.name', read_only=True
    )

    class Meta:
        model = Shop
        fields = (
            "id",
            "name",
            "city",
            "street",
            "house",
            "open_time",
            "close_time",
        )
