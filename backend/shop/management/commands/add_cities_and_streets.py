"""
Содержит скрипт добавления данных городов и улиц в БД.
"""

import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from shop.models import City, Street

PATH_CSV_CITIES = './data/cities.csv'
PATH_CSV_STREETS = './data/streets.csv'


class Command(BaseCommand):
    help = 'Загрузка csv в ДТ'

    def handle(self, *args, **options):
        with open(PATH_CSV_CITIES, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for name in reader:
                City.objects.get_or_create(
                    name=name[0],
                )
        with open(PATH_CSV_STREETS, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for name, city_id in reader:
                Street.objects.get_or_create(
                    name=name,
                    city=get_object_or_404(City, id=city_id)
                )
        self.stdout.write('Города и улицы добавлены')
