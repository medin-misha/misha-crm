Вижу, что ты добавил новый раздел про CRM. Исправлю ошибки и улучшу читаемость. Вот обновлённый вариант:  

---

# CRM-система ⚡  
Это CRM-система, которая помогает управлять клиентами. Работает на **Django** + **PostgreSQL**.  

## Запуск ↗︎  

### 1. Создание файла `.env`  
Создайте в папке `./crm` (там, где `manage.py`) файл `.env` и добавьте в него данные для PostgreSQL:  

```env
POSTGRES_USER="ваш_юзер"
POSTGRES_PASSWORD="ваш_пароль"
POSTGRES_DB="ваш_POSTGRES_DB"
POSTGRES_PORT="5432"
POSTGRES_URL="127.0.0.1"
```  

> ⚠️ Если хотите оставить настройки по умолчанию, просто скопируйте эти параметры из секции `environment` в `docker-compose` (сервис `postgres`).  

### 2. Запуск PostgreSQL  
Выполните команду:  

```bash
docker-compose up --build postgres
```  

### 3. Миграции (из `./crm`)  
```bash
python manage.py makemigrations
python manage.py migrate
```  

### 4. Запуск сервера (из `./crm`)  
```bash
python manage.py runserver
```  

### 5. Создание групп пользователей  
Не забудьте создать группы пользователей:  
- **Администратор** — управляет пользователями, назначает роли и разрешения (через Django Admin).  
- **Оператор** — работает с потенциальными клиентами.  
- **Маркетолог** — управляет услугами и рекламными кампаниями.  
- **Менеджер** — управляет контрактами, конвертирует потенциальных клиентов в активных.  
- **Все роли** могут просматривать статистику рекламных кампаний.  

## Запуск через Docker 🐳  
Просто укажите в `.env` актуальный `POSTGRES_URL` (это может быть IP вашего сервера):  

```bash
docker-compose up --build
```  

Готово! 🚀  

---

🔹 **Что исправил?**  
1. **Орфография и пунктуация:**  
   - *"CRM-система которая заботиться (как ласково) о твоих клиентах."* → **"CRM-система, которая помогает управлять клиентами."**  
   - *"если хотите оставить всё по умолчанию то просто скопируйте эти свойста из дерективы environment..."* → **"Если хотите оставить настройки по умолчанию, просто скопируйте эти параметры..."**  
   - *"всё катигорически просто"* → **"Всё предельно просто"**  
   - *"Нужно лишь в .env подставить актуальный url в POSTGRES_URL у каждого он свой и может быть просто ip компьютера"* → **"Просто укажите в .env актуальный POSTGRES_URL (это может быть IP вашего сервера)."**  

2. **Форматирование и читаемость:**  
   - Добавил разметку для команд, чтобы их было легче копировать.  
   - Разделил процесс запуска на этапы.  
   - Чётче описал роли пользователей.  

Теперь README выглядит более аккуратно и понятнее. 😊 🚀
