[![Django test](https://github.com/Ilyneke/Places_Remember/actions/workflows/django.yml/badge.svg?branch=master)](https://github.com/Ilyneke/Places_Remember/actions/workflows/django.yml)


### Places remember - сайт на котором вы можете сохранять свои впечатления о посещаемых местах

quick start:
1. Создайте локальную копию репозитория
`git clone https://github.com/Ilyneke/Places_Remember.git`
2. Запустите контейнер
`docker-compose up -d`
3. Сайт должен быть доступен по ссылке localhost:8000

Приложение реализовано на базе фреймворка Django, для работы с картой использовался JavaScript.
Оформление кода соответствует стандартам (PEP8, Django coding style).
Все используемые зависимости актуальны на момент создания проекта.
Основной функционал (создание впечатлений о посещаемых местах и получение их списка) покрыт юнит-тестами.
Для стилей используется bootstrap.
Запуск тестов при новых коммитах реализован с использованием github actions.
Локальный запуск через docker/docker-compose.
