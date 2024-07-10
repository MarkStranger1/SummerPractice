# Generated by Django 5.0.6 on 2024-07-06 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'default_related_name': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'default_related_name': 'Streets',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('house', models.PositiveSmallIntegerField(verbose_name='Номер дома')),
                ('open_time', models.TimeField(verbose_name='Время открытия')),
                ('close_time', models.TimeField(verbose_name='Время закрытия')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'default_related_name': 'Shops',
            },
        ),
        migrations.AddConstraint(
            model_name='street',
            constraint=models.UniqueConstraint(fields=('name', 'city'), name='unique_street_city'),
        ),
    ]
