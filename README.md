# Кошачий благотворительный фонд (0.1.0)

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии

 - Python 3.7
 - FastAPI
 - SQLAlchemy
 - Pydantic
 - Alembic
 - Uvicorn

## Установка

Клонируйте репозиторий на ваш компьютер, в локальном репозитории создайте и активируйте виртуальное окружение, обновите менеджер пакетов pip и установите зависимости из файла requirements.txt.

```bash
git clone <адрес репозитория>
python -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Использование

В корне проекта создайте файл переменных окружения `.env` со следующими переменными:
```
APP_TITLE=< Название приложения >
DATABASE_URL=< БД (по умолчанию sqlite+aiosqlite) >
APP_DESCRIPTION=< Описание приложения >
SECRET=< Cекретный ключ >

FIRST_SUPERUSER_EMAIL=admin@adm.ru
FIRST_SUPERUSER_PASSWORD=string
```
Примените миграции:
```bash
alembic upgrade head
```
Запуск приложения:
```
uvicorn app.main:app --reload
```

После запуска приложения будет доступна документация по следующим адресам: </br>
- http://127.0.0.1:8000/docs (документация Swagger)
- http://127.0.0.1:8000/redoc (документация Redoc)

# API google

В приложении QRKot есть возможность формирования отчёта в гугл-таблице. 
В ней указаны закрытые проекты, отсортированные по скорости сбора средств 
— от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

![alt text](https://pictures.s3.yandex.net/resources/image_1716186851.png)

Добавте  ключи, в файле .env:

```python
EMAIL=example@gmail.com - Ваш email от учетной записи Гугл
```

Далее файл необходимо заполнить согласно полученного Json ключа в Google Cloud Platform создав сервисный аккаунт. <https://console.cloud.google.com/projectselector2/home/dashboard>

И подключить два API - ```Google Drive API``` и ```Google Sheets API```.

```python
TYPE=type
PROJECT_ID=project_id
PRIVATE_KEY_ID=private_key_id
PRIVATE_KEY='-----BEGIN PRIVATE KEY-----\-----END PRIVATE KEY-----\n'
CLIENT_EMAIL=xxx.gserviceaccount.com
CLIENT_ID=client_id
AUTH_URI=https://
TOKEN_URI=https://
AUTH_PROVIDER_X509_CERT_URL=https://
CLIENT_X509_CERT_URL=https://
```



## Авторство

Автор проекта: Шуликин Алексей. Проект создан во время обучения в Яндекс Практикуме.