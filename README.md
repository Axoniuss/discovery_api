# Сайт

https://river33.pythonanywhere.com/
<img width="549" height="320" alt="Снимок экрана от 2025-10-23 09-40-26" src="https://github.com/user-attachments/assets/e898b2ef-702b-49ce-96c4-5980d7cf5f3b" />


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
