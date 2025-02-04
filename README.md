# Магазины в городе

### Задача проекта
Реализовать сервис, который принимает и отвечает на HTTP запросы. Полное задание доступно по [ссылке](https://drive.google.com/file/d/1nTTSmdbbJPnTCC3_Pi0oeIc5oFXFW0K2/view).


### Разработчик
Титов Артем Сергеевич, студент 3 курса Самарского университета.


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
