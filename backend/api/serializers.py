"""
Содержит преобразователи данных(сериализаторы) для моделей:

- City;
- Street;
- Shop.
"""

from rest_framework import serializers
from shop.models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):
    """Преобразование данных модели City."""

    class Meta:
        model = City
        fields = (
            "id",
            "name",
        )


class ShortStreetSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Short."""

    class Meta:
        model = Street
        fields = (
            "id",
            "name",
        )


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
