# CRM система

## как запустить?
Для начала нужно создать в ./crm файл .env (там где manage.py) и вставить туда Данные POSTGRES:
```env
POSTGRES_USER = "ваш юзер"
POSTGRES_PASSWORD = "ваш пароль"
POSTGRES_DB = "ваш POSTGRES_DB"
POSTGRES_PORT = "5432"
POSTGRES_URL = "127.0.0.1"
```
Если хотите оставит всё по умолчанию то просто скопируйте эти свойста из дерективы environment в docker-compose в сервисе postgres.

Теперь миграции (из ./crm):
```commandline
python manage.py makemigrations
python manage.py migrate
```
и запуск (из ./crm):
```commandline
python manage.py runserver
```
вот.