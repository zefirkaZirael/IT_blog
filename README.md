# Django Blog

Простое блог-приложение на Django с регистрацией, статьями и комментариями.

## Установка

1. Клонируй репозиторий:

```bash
    git clone <ссылка>
    cd <папка_проекта>
```
При желании активируй вирутальное окржение: 
```
    python -m venv venv
    venv\Scripts\activate       # Windows
```
2. Установи зависимости:
``` 
    pip install django
```
4. Применить миграции:
```
    python manage.py makemigrations
    python manage.py migrate
```
5. Создай суперпользователя:
```
    python manage.py createsuperuser
```
6. Запусти сервер:

```
    python manage.py runserver
```

7. Перейди в браузере:

Главная: http://127.0.0.1:8000/

Админка: http://127.0.0.1:8000/admin
