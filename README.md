# Discovery API

Backend API для интерактивной карты мест Москвы.

## Описание

Django REST API для управления и отображения географических мест на карте. 
Включает административный интерфейс для управления контентом.

## Функциональность

- REST API для мест и изображений
- Админка с WYSIWYG-редактором
- Загрузка и превью изображений
- GeoJSON endpoint для карт
- Переменные окружения для конфигурации

## Технологии

- Python 3.8
- Django 4.2.7


## Установка

bash
# Клонирование
git clone https://github.com/Axoniuss/discovery_api.git
cd discovery_api

# Виртуальное окружение
python -m venv venv
source venv/bin/activate

# Зависимости
pip install -r requirements.txt

# Миграции
python manage.py migrate

# Суперпользователь
python manage.py createsuperuser

# Запуск
python manage.py runserver
