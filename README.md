# Магазины в городе

### Описание проекта
"Магазины в городе" — это веб-сервис, который позволяет пользователям находить информацию о магазинах в их городе. Сервис предоставляет возможность получать данные о городах, улицах и магазинах, а также фильтровать магазины по различным критериям.

### Задача проекта
Реализовать сервис, который принимает и отвечает на HTTP запросы.


### Разработчик
[Титов Артем](https://github.com/MarkStranger1), студент 3 курса Самарского университета


## Модели данных

### Магазин (Shop):

- **id** (Integer): Автоматически генерируемый уникальный идентификатор.
- **name** (String): Название магазина.
- **city** (ForeignKey to `City`): Ссылка на город, в котором находится магазин.
- **street** (ForeignKey to `Street`): Ссылка на улицу, на которой находится магазин.
- **house** (String): Номер дома, в котором находится магазин.
- **open_time** (Time): Время открытия магазина.
- **close_time** (Time): Время закрытия магазина.

### Город (City):

- **id** (Integer): Автоматически генерируемый уникальный идентификатор.
- **name** (String): Название города.

### Улица (Street):

- **id** (Integer): Автоматически генерируемый уникальный идентификатор.
- **name** (String): Название улицы.
- **city** (ForeignKey to `City`): Ссылка на город, в котором находится улица.



## Запуск проекта

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/MarkStranger1/SummerPractice.git
```

2. Перейдите в каталог проекта:
```bash
cd SummerPractice
```

3. Создайте файл .env в `/infra`, используя шаблон `/infra/.env.example`.

4. Перейдите в `backend/`:
```bash
cd backend
```

5. Создайте виртуальное окружение:
```bash
poetry shell
```

6. Установите все зависимости:
```bash
poetry install
```

### Запуск

1. Перейдите в `infra/`:
```bash
cd ../infra/
```

2. Запустите docker-compose:
```bash
docker compose up -d --build
```

3. Выполните миграции внутри контейнера:
```bash
docker-compose exec backend python manage.py migrate
```

* Вы можете загрузить небольшой объем данных в БД:
```bash
docker-compose exec backend python manage.py add_cities_and_streets
```

Проект будет доступен по адресу: http://localhost/.  
API проекта: http://localhost/api/.

## Запросы

|Описание|Адрес|Тип|Результат|Тело|
|:----:|:----:|:----:|:----:|:----:|
|City|`http://localhost/api/city/`|GET|Получение городов|-|
|Street|`http://localhost/api/city/<city_id>/street/`|GET|Получение улиц города по id|-|
|Shop|`http://localhost/api/shop/?city=&street=&open=`|GET|Получение магазинов с возможностью фильтрации по названию города(city), названию улицы(street) и работы магазина(open), где 0 - закрыто, 1 открыто|-|
|Shop|`http://localhost/api/shop/`|POST|Создание магазина|{`"name": "string", "street": "street_id", "house": "int", "open_time": "HH:MM:SS", "close_time": "HH:MM:SS"`}|

