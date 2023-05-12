# Blog - [Github repository](https://github.com/ghettoDdOS/blog)
Блог - это проект в рамках курса "Облачные и мобильные технологии", который представляет из себя REST API блога с возможностью регистрации, ведения блога и комментариев, созданный с использованием фреймворков Django и Django Rest в качестве инструментов для разработки REST API.

## Технологии, используемые в проекте

- Python
- Django
- Django REST Framework
- API REST
- sqlite3
- openapi
- swagger
- poetry

## Установка

1. В качестве пакетного менеджера в проекте используется [Poetry]([https://](https://python-poetry.org/docs/)), установите его следуя документации.
2. Установите зависимости проекта `poetry install`
3. Выполните миграции в локальную базу данных `poetry run python manage.py migrate`
4. Создайте локального администратора `poetry run python manage.py createsuperuser`

### Запуск

- Для запуска локального сервера используйте команду `poetry run python manage.py runserver localhost:8000`
- Для доступа к административной панели перейдите по адресу [localhost:8080/admin](http://localhost:8080/admin)

## Документация API

Для доступа к документации в формате Swagger Openapi перейдите по адресу [localhost:8080/api/docs](http://localhost:8080/api/docs)
