"""
Содержит View-классы реализующие операции моделей:

- City;
- Shop.
"""

from django.shortcuts import get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shop.models import City, Shop, Street

from .filters import ShopFilter
from .serializers import (CitySerializer, ShopReadSerializer,
                          ShopWriteSerializer, ShortStreetSerializer)


"""
Определяет CityViewSet, который предоставляет API для следующих операций:

- `GET /cities/`: Перечислить все города
- `GET /cities/<pk>/`: Получить информацию о конкретном городе по id
- `GET /cities/<pk>/street/`: Получить список улиц, принадлежащих городу с указанным id

CitySerializer и ShortStreetSerializer предоставляют сериализацию объектов City и Street соответственно
"""


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """View-класс реализующий операции модели City."""

    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(detail=True, methods=['get'])
    def street(self, request, pk):
        """Получение улиц принадлежащих определенному городу по id."""
        streets = get_list_or_404(Street, city__id=pk)
        serializer = ShortStreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopViewSet(viewsets.ModelViewSet):
    """View-класс реализующий операции модели Shop."""

    queryset = Shop.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    """
    Определяем метод get_serializer_class в классе, который является классом ViewSet в Django REST Framework
    """
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShopReadSerializer
        return ShopWriteSerializer

    """
    Типичный пример функции create для представления REST API 
    с использованием фреймворка Django REST Framework (DRF)
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'id': serializer.data['id']},
                        status=status.HTTP_201_CREATED)
