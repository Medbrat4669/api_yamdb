# Yamdb Project
Проект студентов Яндекс.Практикум по курсу 'API: интерфейс взаимодействия программ'

Описание:

Проект Yamdb собирает отзывы пользователей на произведения.
Произведения делятся на: "Категории", "Фильмы", "Музыка".
Список категорий может быть расширен администратором.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории "Книги" могут быть произведения "Скотный двор" и "Гарри Поттер и философский камень", а в категории "Музыка" — песня "I'm Lost" группы "The Irrepressibles " и песня "Стильный Ай" исполнителя "Feduk".
Произведению может быть присвоен жанр из списка предустановленных.
Новые жанры может создавать только администратор.
Пользователи могут оставить к произведениям отзыв и оценку в диапазоне от одного до десяти, а из пользовательских оценок формируется средний рейтинг.
## Доступный функционал:
Для аутентификации используются JWT-токены.
У неаутентифицированных пользователей доступ к API только на уровне чтения.
Создание объектов разрешено только аутентифицированным пользователям.
На прочий фунционал наложено ограничение в виде административных ролей и авторства.
Управление пользователями.
Получение списка всех категорий и жанров, добавление и удаление.
Получение списка всех произведений, их добавление.
Получение, обновление и удаление конкретного произведения.
Получение списка всех отзывов, их добавление.
Получение, обновление и удаление конкретного отзыва.
Получение списка всех комментариев, их добавление.
Получение, обновление и удаление конкретного комментария.
Возможность получения подробной информации о себе и удаления своего аккаунта.
Фильтрация по полям.
Документация к API доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера с проектом.
## Технологии:
Python 3.7
Django 2.2.16
Django Rest Framework 3.12.4
Simple JWT
SQLite3
Запуск проекта в dev-режиме

Склонируйте репозиторий:
git clone <название репозитория>
Установите и активируйте виртуальное окружение:
python -m venv venv

Windows:
source venv/Scripts/activate

MacOS:
source venv/bin/activate

Установите зависимости из файла requirements.txt:
pip install -r requirements.txt
Перейдите в папку api_yamdb/api_yamdb.
Примените миграции:
python manage.py migrate
Загрузите тестовые данные:
python manage.py load_csv_data
Выполните команду:
python manage.py runserver
## Примеры некоторых запросов API:
Регистрация пользователя:
POST /api/v1/auth/signup/

Получение данных своей учетной записи:
GET /api/v1/users/me/

Добавление новой категории:
POST /api/v1/categories/

Удаление жанра:
DELETE /api/v1/genres/{slug}

Частичное обновление информации о произведении:
PATCH /api/v1/titles/{titles_id}

Получение списка всех отзывов:
GET /api/v1/titles/{title_id}/reviews/

Добавление комментария к отзыву:
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

Полный список запросов API находятся в документации.
## Авторы:
Воронович Кирилл - https://github.com/c0der21
Лифанов Дмитрий- https://github.com/Dimalright
Чугин Владислав
