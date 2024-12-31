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
Запустить postgres можно легко командой:
```commandline
docker-compose up --build postgres
```
Если хотите оставить всё по умолчанию то просто скопируйте эти свойста из дерективы environment в docker-compose в сервисе postgres.

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
### Работа, группы:
В приложеных фотокарточках есть все группы пользователей. Их извольте создать сами.
### как запустить через docker
всё катигорически просто. Нужно лишь в .env подставить актуальный url в POSTGRES_URL у каждого он свой и может быть просто ip компьютера:
```commandline
docker compose up --build
```