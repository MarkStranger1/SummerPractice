"""
Содержит роутеры для API.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('city', views.CityViewSet, basename='cities')
router.register(
    r'city/(?P<city_id>\d+)/street',
    views.CityViewSet,
    basename='city-street'
)
router.register('shop', views.ShopViewSet, basename='shops')


urlpatterns = [
    path('', include(router.urls)),
]
